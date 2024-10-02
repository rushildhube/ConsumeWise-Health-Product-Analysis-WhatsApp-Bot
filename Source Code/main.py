from flask import Flask, request
import pickle
import requests
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from fetch_product_details import fetch_product_by_barcode, display_product_info, check_allergies
from check_misleading_claims import analyze_claim
from config import ALLERGEN_MAP
from config import nova_data
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

# For session management
user_sessions = {}

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

def collect_patient_data(user_id, incoming_msg):
    """Collects patient data and stores it in the user session."""
    session = user_sessions[user_id]
    if 'collecting_diabetes' not in session:
        # Ask if user has diabetes
        session['collecting_diabetes'] = True
        session['collecting_allergies'] = False
        session['collecting_user_allergies'] = False
        session['health_profile'] = {}
        response = "Do you have diabetes? (yes/no): "
        return response
    elif session['collecting_diabetes']:
        # Store the response
        diabetes = incoming_msg.strip().lower()
        session['health_profile']['Diabetes'] = diabetes
        session['collecting_diabetes'] = False
        session['collecting_allergies'] = True
        response = "Do you have any allergies? (yes/no): "
        return response
    elif session['collecting_allergies']:
        allergies = incoming_msg.strip().lower()
        session['health_profile']['Allergies'] = []
        if allergies == 'yes':
            session['collecting_user_allergies'] = True
            response = "Enter any allergies you have, separated by commas: "
        else:
            session['collecting_user_allergies'] = False
            response = "Thank you! Your health profile has been updated."
            # Now proceed to main menu
            session['state'] = 'main_menu'
            response += "\n" + get_main_menu()
        session['collecting_allergies'] = False
        return response
    elif session['collecting_user_allergies']:
        user_allergies = incoming_msg.strip()
        session['health_profile']['Allergies'] = [allergy.strip().lower() for allergy in user_allergies.split(',')]
        session['collecting_user_allergies'] = False
        response = "Thank you! Your health profile has been updated."
        # Now proceed to main menu
        session['state'] = 'main_menu'
        response += "\n" + get_main_menu()
        return response

def get_main_menu():
    menu = "\n--- Main Menu ---\n"
    menu += "1. Search product by barcode\n"
    menu += "2. Check for misleading claims by barcode\n"
    menu += "3. Check processing level by barcode\n"
    menu += "4. Exit\n"
    menu += "\nChoose an option (1-4): "
    return menu

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

def predict_processing_level(barcode):
    """Predict the processing level based on ingredients."""
    # Load the trained model and vectorizer
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    with open('vectorizer.pkl', 'rb') as vec_file:
        vectorizer = pickle.load(vec_file)

    product_name, ingredients, nova_custom_label = prepare_data(barcode)

    if ingredients == 'No ingredients available':
        # Since we can't prompt the user, we return an error
        return "Ingredients not found for this product."

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

    response = f"Product Name: {product_name}\n"
    response += f"Ingredients: {ingredients}\n"
    response += f"Predicted Processing Level (Model): {predicted_class}\n"
    response += f"Actual Custom NOVA Classification: {nova_custom_label}"
    return response

def main_menu_selection(user_id, incoming_msg):
    session = user_sessions[user_id]
    choice = incoming_msg.strip()
    if choice == '1':
        session['state'] = 'option_1'
        response = "Enter the product barcode: "
    elif choice == '2':
        session['state'] = 'option_2'
        response = "Enter the product barcode to check for misleading claims: "
    elif choice == '3':
        session['state'] = 'option_3'
        response = "Enter the product barcode: "
    elif choice == '4':
        response = "Exiting the tool. Goodbye!"
        session['state'] = 'exit'
    else:
        response = "Invalid option, please try again.\n" + get_main_menu()
    return response

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').strip()
    user_id = request.values.get('From', '')
    # Initialize session for the user if not exists
    if user_id not in user_sessions:
        user_sessions[user_id] = {'state': 'collect_patient_data'}
        response = "Welcome to the Food Health Analysis Tool!\nCollecting patient data..."
    else:
        response = ''
    session = user_sessions[user_id]
    state = session.get('state', 'collect_patient_data')
    if state == 'collect_patient_data':
        response += '\n' + collect_patient_data(user_id, incoming_msg)
    elif state == 'main_menu':
        response += '\n' + main_menu_selection(user_id, incoming_msg)
    elif state == 'option_1':
        # Process option 1: Search product by barcode
        barcode = incoming_msg.strip()
        product = fetch_product_by_barcode(barcode)
        if product:
            health_profile = session['health_profile']
            product_info = analyze_product_health(product)
            suitability_score, reasons = calculate_suitability_score(product, health_profile)
            response += "\n--- Product Analysis ---\n"
            response += f"Harmful Ingredients: {product_info['harmful_ingredients']}\n"
            response += f"Nutritional Deficiencies: {product_info['nutritional_deficiencies']}\n"
            response += f"Suitability Score: {suitability_score}\n"
            response += f"Reasons for Score: {reasons}\n"
        else:
            response += "No product information available."
        # After processing, go back to main menu
        response += "\n" + get_main_menu()
        session['state'] = 'main_menu'
    elif state == 'option_2':
        # Process option 2: Check for misleading claims
        if 'barcode' not in session:
            barcode = incoming_msg.strip()
            session['barcode'] = barcode
            response += "Enter the claim to analyze (e.g., height growth, strength increase): "
        else:
            barcode = session['barcode']
            claim = incoming_msg.strip()
            product = fetch_product_by_barcode(barcode)
            if product:
                ingredients = product.get('ingredients_text', '')
                if ingredients:
                    analysis = analyze_claim(claim, ingredients)
                    if analysis:
                        response += "\nClaim Analysis Result:\n"
                        if isinstance(analysis, dict):
                            for key, value in analysis.items():
                                response += f"{key}: {value}\n"
                        else:
                            response += f"Error analyzing claim: {analysis}\n"
                    else:
                        response += "Could not retrieve claim analysis."
                else:
                    response += "No ingredients information available for the product."
            else:
                response += "No product information available."
        
            response += "\n" + get_main_menu()
            session['state'] = 'main_menu'
            session.pop('barcode', None)
    elif state == 'option_3':
        # Process option 3: Check processing level by barcode
        barcode = incoming_msg.strip()
        processing_info = predict_processing_level(barcode)
        response += processing_info
        # After processing, go back to main menu
        response += "\n" + get_main_menu()
        session['state'] = 'main_menu'
    elif state == 'exit':
        response += "Thank you for using the Food Health Analysis Tool. Goodbye!"
        # Reset session or delete it
        user_sessions.pop(user_id, None)
    else:
        response += "Sorry, I didn't understand that. Please try again."
    # Send the response back to the user
    twilio_response = MessagingResponse()
    twilio_response.message(response)
    return str(twilio_response)

if __name__ == '__main__':
    app.run(debug=True)
