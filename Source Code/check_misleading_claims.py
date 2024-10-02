import requests


def fetch_product_by_barcode(barcode):
    """Fetch product information from Open Food Facts using the barcode."""
    if not barcode:
        print("No barcode provided.")
        return None

    url = f'https://world.openfoodfacts.org/api/v0/product/{barcode}.json'
    try:
        response = requests.get(url)
        response.raise_for_status()
        product_info = response.json()
        if product_info.get('status') == 1:
            return product_info.get('product', {})
        else:
            print("Product not found.")
            return None
    except requests.RequestException as e:
        print(f"Failed to retrieve product information: {e}")
        return None


import requests

def analyze_claim(claim, ingredients):
    """Analyze the claim based on the product's ingredients."""
    api_url = "https://cwbackend-a3332a655e1f.herokuapp.com/claims/analyze"
    params = {
        'claim': claim,
        'ingredients': ingredients
    }

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        return response.json()  # Ensure this returns a dictionary
    except requests.RequestException as e:
        print(f"Failed to analyze claim: {e}")
        return {"error": "Could not retrieve claim analysis."}


def main():
    print("Welcome to the Misleading Claims Checker!")

    barcode = input("Enter the product barcode to search: ").strip()
    claim = input("Enter the claim to analyze (e.g., height growth, strength increase): ").strip()

    product = fetch_product_by_barcode(barcode)

    if product:
        ingredients = product.get('ingredients_text', 'Ingredients information not available')
        product_name = product.get('product_name', 'Unnamed product')

        print(f"\nProduct selected: {product_name}")
        print(f"Ingredients: {ingredients}")

        if ingredients:
            analysis = analyze_claim(claim, ingredients)
            if analysis:
                print("\nClaim Analysis Result:")
                for key, value in analysis.items():
                    print(f"{key}: {value}")
            else:
                print("Could not retrieve claim analysis.")
        else:
            print("Could not retrieve ingredients.")
    else:
        print("No product found for the given barcode.")


if __name__ == "__main__":
    main()
