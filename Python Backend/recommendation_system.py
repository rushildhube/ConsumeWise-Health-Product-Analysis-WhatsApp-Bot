import requests
import json


# Fetch product details using the barcode
def get_product_data(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)
    if response.status_code == 200:
        product_data = response.json().get('product', {})
        if product_data:
            product_name = product_data.get('product_name', 'Unknown Product')
            ingredients = product_data.get('ingredients_text', 'Ingredients not available')
            nova_group = product_data.get('nova_group', 'Unknown')
            print(f"Product Name: {product_name}")
            print(f"Ingredients: {ingredients}")
            print(f"NOVA Group: {nova_group}")
        return product_data
    else:
        print("Product not found!")
        return {}


# Extract nutritional information (calories, fats, sodium)
def extract_nutritional_info(product_data):
    nutriments = product_data.get('nutriments', {})
    calories = nutriments.get('energy_100g', 0)
    fats = nutriments.get('fat_100g', 0)
    sodium = nutriments.get('sodium_100g', 0)
    return {
        'calories': calories,
        'fats': fats,
        'sodium': sodium
    }


# Classify the product based on its category
def classify_product(product_data):
    categories = product_data.get('categories_tags', [])
    if categories:
        print(f"Product Category: {categories[0]}")
        return categories
    return ["Unknown Category"]


# Fetch other products from the same category
def get_products_by_category(category):
    url = f"https://world.openfoodfacts.org/category/{category}.json?lc=en"  # English localization
    response = requests.get(url)
    if response.status_code == 200:
        products = response.json().get('products', [])
        print(f"Found {len(products)} products in category '{category}'")
        return products
    else:
        print(f"Could not retrieve products for category {category}")
        return []


# Recommend healthier alternatives based on NOVA group less than 3
def recommend_healthier_product(original_product_data, all_products_data):
    original_nutritional_info = extract_nutritional_info(original_product_data)
    original_nova_group = original_product_data.get('nova_group', 0)
    healthier_alternatives = []

    for product in all_products_data:
        # Skip if the product is the original one or missing nutritional data
        if product == original_product_data or not product.get('nutriments'):
            continue

        nova_group = product.get('nova_group', 0)
        if nova_group and nova_group < 3:  # Only consider NOVA group less than 3
            nutritional_info = extract_nutritional_info(product)
            product_name = product.get('product_name', 'Unknown')

            # Check if calories, fats, and sodium are lower than the original product
            if (nutritional_info['calories'] < original_nutritional_info['calories'] and
                    nutritional_info['fats'] < original_nutritional_info['fats'] and
                    nutritional_info['sodium'] < original_nutritional_info['sodium']):
                print(f"Checking product: {product_name}")
                healthier_alternatives.append({
                    'product_name': product_name,
                    'calories': nutritional_info['calories'],
                    'fats': nutritional_info['fats'],
                    'sodium': nutritional_info['sodium'],
                    'nova_group': nova_group
                })

    return healthier_alternatives


# Load fallback healthier alternatives from JSON, filtered by NOVA group
def load_fallback_alternatives():
    try:
        with open('fallback_alternatives.json', 'r') as file:
            fallback_data = json.load(file)

            # Filter out products with NOVA group 3 or above
            for category, products in fallback_data.items():
                fallback_data[category] = [p for p in products if p['nova_group'] < 3]

            return fallback_data
    except FileNotFoundError:
        print("Fallback alternatives file not found.")
        return {}


# Recommend healthier alternatives or fallback to JSON
def recommend_healthier_alternatives(barcode):
    # Fetch the original product data
    original_product = get_product_data(barcode)

    if not original_product:
        print("Original product not found!")
        return []  # Return an empty list if no product is found

    # Classify the product
    original_category = classify_product(original_product)
    if not original_category:
        print("Could not classify the product")
        return []  # Return an empty list if no category found

    # Fetch products in the same category
    category_products = get_products_by_category(original_category[0])  # Use the first category

    if not category_products:  # Check if category products were found
        print(f"No products found in category '{original_category[0]}'")
        return []  # Return an empty list if no category products are found

    # Recommend healthier alternatives
    healthier_products = recommend_healthier_product(original_product, category_products)

    if healthier_products:  # If we found healthier products, return them
        print("\nHealthier alternatives found:")
        for product in healthier_products:
            print(
                f"Product: {product['product_name']}, Calories: {product['calories']}, Fats: {product['fats']}, Sodium: {product['sodium']}, NOVA Group: {product['nova_group']}")
        return healthier_products  # Return the list of healthier products
    else:
        # No alternatives found, use fallback
        print("No healthier alternatives found. Using fallback alternatives.")
        fallback_alternatives = load_fallback_alternatives()
        category = original_category[0].capitalize() if original_category else "Unknown"

        if category in fallback_alternatives:
            print(f"\nFallback healthier alternatives for {category}:")
            for product in fallback_alternatives[category]:
                print(
                    f"Product: {product['product_name']}, Calories: {product['calories']}, Fats: {product['fats']}, Sodium: {product['sodium']}, NOVA Group: {product['nova_group']}")
            return fallback_alternatives[category]  # Return fallback alternatives
        else:
            print(f"No fallback alternatives available for category '{category}'")
            return []  # Return an empty list if no fallback alternatives are available


# Input: barcode from user
if __name__ == "__main__":
    barcode_input = input("Enter the barcode of the product: ")
    recommend_healthier_alternatives(barcode_input)
