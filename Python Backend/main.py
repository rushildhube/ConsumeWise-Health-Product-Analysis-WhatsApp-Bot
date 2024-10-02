import pickle
import requests
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from fetch_product_details import fetch_product_by_barcode, display_product_info, check_allergies
from check_misleading_claims import analyze_claim
from config import ALLERGEN_MAP, nova_data
from recommendation_system import get_product_data, recommend_healthier_alternatives  # Import functions

# Load local ingredients data file path
local_data_file = 'ingredients_data.json'


def load_local_ingredients():
    """Load ingredients data from a JSON file."""
    try:
        with open(local_data_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_local_ingredients(data):
    """Save ingredients data to a JSON file."""
    with open(local_data_file, 'w') as file:
        json.dump(data, file)


def collect_patient_data():
    """Collects patient data and returns it as a dictionary."""
    print("Collecting patient data...")
    diabetes = input("Do you have diabetes? (yes/no): ").strip().lower()

    allergies = input("Do you have any allergies? (yes/no): ").strip().lower()
    user_allergies = input("Enter any allergies you have, separated by commas: ").strip() if allergies == 'yes' else ''

    return {
        'Diabetes': diabetes,
        'Allergies': [allergy.strip().lower() for allergy in user_allergies.split(',')] if user_allergies else []
    }


def analyze_product_health(product):
    """Analyzes the health of a product based on its nutritional information and ingredients."""
    harmful_ingredients = []
    nutritional_deficiencies = []

    ingredients = product.get('ingredients_text', '')
    if 'sugar' in ingredients.lower():
        harmful_ingredients.append('Sugar')

    nutriments = product.get('nutriments', {})
    sugar = float(nutriments.get('sugars', 0))
    fat = float(nutriments.get('fat', 0))
    sodium = float(nutriments.get('salt', 0))

    if sugar > 5:
        nutritional_deficiencies.append('High sugar content')
    if fat > 10:
        nutritional_deficiencies.append('High fat content')
    if sodium > 1:
        nutritional_deficiencies.append('High sodium content')

    return {
        "harmful_ingredients": harmful_ingredients,
        "nutritional_deficiencies": nutritional_deficiencies
    }


def calculate_suitability_score(product, health_profile):
    """Calculates the suitability score of a product based on the user's health profile and product details."""
    suitability_score = 10
    reasons = []

    ingredients = product.get('ingredients_text', '').lower()
    nutriments = product.get('nutriments', {})
    sugar = float(nutriments.get('sugars', 0))
    fat = float(nutriments.get('fat', 0))
    sodium = float(nutriments.get('salt', 0))

    # Check for harmful ingredients
    if 'sugar' in ingredients:
        suitability_score -= 3
        reasons.append("Contains sugar.")

    if sugar > 5:
        suitability_score -= 2
        reasons.append("High sugar content.")
    if fat > 10:
        suitability_score -= 2
        reasons.append("High fat content.")
    if sodium > 1:
        suitability_score -= 2
        reasons.append("High sodium content.")

    # Check allergens
    allergens = product.get('allergens_tags', [])
    found_allergens = []

    for allergen in health_profile['Allergies']:
        if allergen in ALLERGEN_MAP:
            allergen_list = ALLERGEN_MAP[allergen]
            if any(a in ingredients for a in allergen_list) or any(a in allergens for a in allergen_list):
                suitability_score = 0
                found_allergens.append(allergen)

    if found_allergens:
        reasons.append("Contains allergens from your allergy profile.")

    # Check diabetes
    if health_profile.get('Diabetes') == 'yes' and sugar > 5:
        suitability_score -= 3
        reasons.append("Not suitable for diabetics.")

    # Ensure the suitability score does not go below zero
    return max(suitability_score, 0), ' '.join(reasons) if reasons else 'None'


def map_nova_to_custom(nova_classification):
    """Map the NOVA classification to custom labels."""
    nova_custom = {
        1: 'A UNPROCESSED',
        2: 'B PROCESSED CULINARY INGREDIENTS',
        3: 'C PROCESSED FOOD',
        4: 'D ULTRA-PROCESSED FOOD'
    }
    return nova_custom.get(nova_classification, 'Unknown')


def fetch_product_data(barcode):
    """Fetch product data from the Open Food Facts API."""
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)
    return response.json()


def extract_product_details(product_data, barcode):
    """Extract product name, ingredients, and NOVA classification."""
    product_name = product_data['product'].get('product_name', 'Unknown')

    # Check API response, otherwise fall back to local ingredients dictionary
    ingredients = product_data['product'].get('ingredients_text')
    local_ingredients = load_local_ingredients()
    if not ingredients and barcode in local_ingredients:
        ingredients = local_ingredients[barcode]
    elif not ingredients:
        ingredients = 'No ingredients available'

    nova_classification = product_data['product'].get('nova_group', None)
    return product_name, ingredients, nova_classification


def prepare_data(barcode):
    """Prepare data for prediction."""
    product_data = fetch_product_data(barcode)
    product_name, ingredients, nova_classification = extract_product_details(product_data, barcode)
    nova_custom_label = map_nova_to_custom(nova_classification)
    return product_name, ingredients, nova_custom_label


def preprocess_data(data):
    """Preprocess the ingredients and NOVA classifications for training."""
    ingredients = [item['ingredients'] for item in data]
    nova_classes = [item['nova_classification'] for item in data]

    vectorizer = TfidfVectorizer(stop_words='english')
    ingredient_vectors = vectorizer.fit_transform(ingredients)

    return ingredient_vectors, nova_classes, vectorizer


def train_model(X, y, vectorizer):
    """Train and save the model and vectorizer."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save the trained model and vectorizer
    with open('model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)

    with open('vectorizer.pkl', 'wb') as vec_file:
        pickle.dump(vectorizer, vec_file)


def predict_processing_level(barcode):
    """Predict the processing level based on ingredients."""
    # Load the trained model and vectorizer
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    with open('vectorizer.pkl', 'rb') as vec_file:
        vectorizer = pickle.load(vec_file)

    product_name, ingredients, nova_custom_label = prepare_data(barcode)

    if ingredients == 'No ingredients available':
        ingredients = input("Ingredients not found. Please enter the ingredients: ")

        # Save the new ingredients for the barcode
        local_ingredients = load_local_ingredients()
        local_ingredients[barcode] = ingredients
        save_local_ingredients(local_ingredients)

    ingredients_vector = vectorizer.transform([ingredients])
    predicted_label = model.predict(ingredients_vector)[0]

    # Map predicted label to custom classification
    classification_mapping = {
        1: "Minimally Processed (level 1)",
        2: "Processed Culinary Ingredients (level 2)",
        3: "Processed Food (level 3)",
        4: "Ultra-Processed Food (level 4)"
    }

    predicted_class = classification_mapping.get(predicted_label, "Unknown")

    print(f"Product Name: {product_name}")
    print(f"Ingredients: {ingredients}")
    print(f"Predicted Processing Level (Model): {predicted_class}")
    print(f"Actual Custom NOVA Classification: {nova_custom_label}")
    return nova_custom_label


def main():
    from recommendation_system import recommend_healthier_alternatives, get_product_data

    print("Welcome to the Food Health Analysis Tool!")

    # Preprocess the NOVA data
    X, y, vectorizer = preprocess_data(nova_data)

    # Train the model
    train_model(X, y, vectorizer)

    health_profile = collect_patient_data()

    while True:
        print("\n--- Main Menu ---")
        print("1. Search product by barcode")
        print("2. Check for misleading claims by barcode")
        print("3. Check processing level by barcode")
        print("4. Recommend healthier alternatives")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            barcode = input("Enter barcode: ")
            product_data = fetch_product_data(barcode)
            product_name, ingredients, nova_classification = extract_product_details(product_data, barcode)

            # Analyze the product's health and suitability
            health_analysis = analyze_product_health(product_data['product'])
            suitability_score, reasons = calculate_suitability_score(product_data['product'], health_profile)

            print(f"Product Name: {product_name}")
            print(f"Ingredients: {ingredients}")
            print(f"NOVA Classification: {nova_classification}")
            print(f"Harmful Ingredients: {health_analysis['harmful_ingredients']}")
            print(f"Nutritional Deficiencies: {health_analysis['nutritional_deficiencies']}")
            print(f"Suitability Score: {suitability_score} ({reasons})")


        elif choice == '2':

            barcode = input("Enter the product barcode to check for misleading claims: ").strip()

            product = fetch_product_by_barcode(barcode)

            if product:

                ingredients = product.get('ingredients_text', '')

                if ingredients:

                    print(f"\nIngredients for product: {ingredients}")

                    claim = input("Enter the claim to analyze (e.g., height growth, strength increase): ").strip()

                    analysis = analyze_claim(claim, ingredients)

                    if analysis:

                        print("\nClaim Analysis Result:")

                        if isinstance(analysis, dict):  # Ensure analysis is a dictionary

                            for key, value in analysis.items():
                                print(f"{key}: {value}")

                        else:

                            print("Error analyzing claim:", analysis)

                    else:

                        print("Could not retrieve claim analysis.")

                else:

                    print("No ingredients information available for the product.")

            else:

                print("No product information available.")

        elif choice == '3':
            barcode = input("Enter barcode: ")
            nova_custom_label = predict_processing_level(barcode)


        elif choice == '4':

            barcode = input("Enter the barcode of the product: ")

            # Use get_product_data to fetch the product details

            product_data = get_product_data(barcode)

            # Recommend healthier alternatives using the product data

            if product_data:

                alternatives = recommend_healthier_alternatives(barcode)

                print(f"Healthier alternatives for {product_data['product_name']}:")

                for alternative in alternatives:
                    print(f"- {alternative['product_name']}: "

                          f"Calories: {alternative['calories']}, "

                          f"Fats: {alternative['fats']}, "

                          f"Sodium: {alternative['sodium']}, "

                          f"NOVA Group: {alternative['nova_group']}")

            else:

                print("No product found or unable to recommend alternatives.")

        elif choice == '5':
            print("Exiting the tool. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
