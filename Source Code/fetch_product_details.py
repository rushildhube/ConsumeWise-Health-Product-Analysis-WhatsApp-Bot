import requests
from config import ALLERGEN_MAP

def fetch_product_by_barcode(barcode):
    """Fetch product information from Open Food Facts using the barcode."""
    if not barcode:
        print("Error: No barcode provided.")
        return None

    url = f'https://world.openfoodfacts.org/api/v0/product/{barcode}.json'
    try:
        response = requests.get(url)
        response.raise_for_status()
        product_info = response.json()
        if product_info.get('status') == 1:
            return product_info.get('product', {})
        else:
            print("Error: Product not found.")
            return None
    except requests.RequestException as e:
        print(f"Error: Failed to retrieve product information: {e}")
        return None

def get_nova_description(nova_group):
    """Provides a description for the NOVA group."""
    descriptions = {
        1: "Unprocessed or minimally processed foods.",
        2: "Processed culinary ingredients.",
        3: "Processed foods.",
        4: "Ultra-processed food and drink products."
    }
    try:
        return descriptions[int(nova_group)]
    except (ValueError, KeyError):
        return "Description not available."

def display_product_info(product):
    """Displays the product information in a formatted manner."""
    if not product:
        print("Error: No product data to display.")
        return

    nova_group = product.get('nova_group', 'N/A')
    print("\n--- Product Information ---")
    print(f"Product Name      : {product.get('product_name', 'N/A')}")
    print(f"Brand             : {product.get('brands', 'N/A')}")
    print(f"Ingredients       : {product.get('ingredients_text', 'N/A')}")
    print(f"Categories        : {product.get('categories', 'N/A')}")
    print(f"NOVA Group        : {nova_group} - {get_nova_description(nova_group)}")
    nutriments = product.get('nutriments', {})
    print(f"Energy            : {nutriments.get('energy_kcal', 'N/A')} kcal")
    print(f"Sugar             : {nutriments.get('sugars', 'N/A')} g")
    print(f"Fat               : {nutriments.get('fat', 'N/A')} g")
    print(f"Sodium            : {nutriments.get('salt', 'N/A')} g")
    print("----------------------------")

def check_allergies(product, user_allergies):
    """Checks if the product contains any allergens from the user's allergy profile."""
    product_allergens = product.get('allergens_tags', [])
    found_allergens = []

    for user_allergen in user_allergies:
        # Compare case-insensitive and check for partial matches using the allergen map
        user_allergen = user_allergen.lower()
        for key, related_allergens in ALLERGEN_MAP.items():
            if user_allergen in related_allergens:
                for prod_allergen in product_allergens:
                    if key in prod_allergen.lower():
                        found_allergens.append(user_allergen)
                        break

    if found_allergens:
        return False, found_allergens  # Not suitable and list of allergens found
    return True, []  # Suitable and empty list
