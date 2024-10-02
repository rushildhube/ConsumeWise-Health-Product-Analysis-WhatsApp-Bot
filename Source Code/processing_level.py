import pickle
import requests
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

nova_data = [
    # NOVA 1 examples (Unprocessed or Minimally Processed Foods)
    {'ingredients': 'carrots', 'nova_classification': 1},  # Fresh vegetables
    {'ingredients': 'spinach', 'nova_classification': 1},  # Leafy greens
    {'ingredients': 'banana', 'nova_classification': 1},  # Fresh fruit
    {'ingredients': 'almonds', 'nova_classification': 1},  # Whole nuts
    {'ingredients': 'chicken breast', 'nova_classification': 1},  # Fresh meat
    {'ingredients': 'salmon', 'nova_classification': 1},  # Fresh fish
    {'ingredients': 'brown rice', 'nova_classification': 1},  # Whole grain
    {'ingredients': 'milk', 'nova_classification': 1},  # Fresh milk
    {'ingredients': 'yogurt', 'nova_classification': 1},  # Plain yogurt (minimally processed)
    {'ingredients': 'eggs', 'nova_classification': 1},  # Whole eggs
    {'ingredients': 'potatoes', 'nova_classification': 1},  # Fresh tubers
    {'ingredients': 'whole wheat flour', 'nova_classification': 1},  # Ground flour (minimally processed)

    # NOVA 2 examples (Processed Culinary Ingredients)
    {'ingredients': 'olive oil, salt', 'nova_classification': 2},
    {'ingredients': 'butter, salt', 'nova_classification': 2},
    {'ingredients': 'coconut oil, sugar', 'nova_classification': 2},
    {'ingredients': 'corn oil, salt', 'nova_classification': 2},
    {'ingredients': 'vegetable oil, salt', 'nova_classification': 2},
    {'ingredients': 'honey, sugar', 'nova_classification': 2},

    # NOVA 3 examples (Processed Foods)
    {'ingredients': 'canned beans, salt', 'nova_classification': 3},
    {'ingredients': 'canned tomatoes, salt, sugar', 'nova_classification': 3},
    {'ingredients': 'pickles, vinegar, salt', 'nova_classification': 3},
    {'ingredients': 'tuna in olive oil, salt', 'nova_classification': 3},
    {'ingredients': 'cheese, salt', 'nova_classification': 3},
    {'ingredients': 'salted peanuts, sugar', 'nova_classification': 3},
    {'ingredients': 'bread, wheat flour, salt', 'nova_classification': 3},
    {'ingredients': 'yogurt, sugar, fruit puree', 'nova_classification': 3},

    # NOVA 4 examples (Ultra-Processed Foods)
    {'ingredients': 'high fructose corn syrup, artificial flavoring, emulsifiers', 'nova_classification': 4},  # Sweetened beverage
    {'ingredients': 'hydrogenated vegetable oil, sugar, salt, artificial colors', 'nova_classification': 4},  # Snack food
    {'ingredients': 'instant noodles, flavor enhancers, preservatives', 'nova_classification': 4},  # Instant noodle product
    {'ingredients': 'processed cheese, emulsifiers, preservatives', 'nova_classification': 4},  # Processed cheese slices
    {'ingredients': 'soft drink, carbonated water, high fructose corn syrup, citric acid', 'nova_classification': 4},  # Soft drink
    {'ingredients': 'candy, sugar, artificial flavors, colorings', 'nova_classification': 4},  # Candy
    {'ingredients': 'frozen pizza, hydrogenated fats, preservatives, flavorings', 'nova_classification': 4},  # Frozen pizza
    {'ingredients': 'breakfast cereal, sugar, artificial vitamins, flavorings', 'nova_classification': 4}  # Sugary breakfast cereal
]

# Local ingredients data file path
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


def map_nova_to_custom(nova_classification):
    """Map the NOVA classification to custom labels."""
    nova_custom = {
        1: 'A UNPROCESSED',
        2: 'B PROCESSED CULINARY INGREDIENTS',
        3: 'C PROCESSED FOOD',
        4: 'D ULTRA-PROCESSED FOOD'
    }
    return nova_custom.get(nova_classification, 'Unknown')


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


def train_model(X, y):
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


if __name__ == "__main__":
    barcode = input("Enter product barcode: ")
    predict_processing_level(barcode)
