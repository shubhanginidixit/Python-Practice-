import json
import os

def filter_products_by_price(input_file, output_file, min_price):
    """
    Reads a JSON file containing product information, filters out products
    below min_price, and writes the result to a new JSON file.
    """
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found!")
        return

    # Read JSON file
    with open(input_file, 'r', encoding='utf-8') as infile:
        try:
            products = json.load(infile)
        except json.JSONDecodeError:
            print(f"Error: File '{input_file}' is not valid JSON.")
            return

    # Filter products
    filtered_products = [
        product for product in products
        if float(product.get("price", 0)) >= min_price
    ]

    # Write filtered data to new JSON file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(filtered_products, outfile, indent=4, ensure_ascii=False)

    print(f"Filtered products saved to '{output_file}'.")


if __name__ == "__main__":
    print("=== Product Filter Script ===")
    input_file = input("Enter input JSON file path (e.g., products.json): ").strip()
    output_file = input("Enter output JSON file path (e.g., filtered_products.json): ").strip()
    
    while True:
        try:
            min_price = float(input("Enter minimum price to filter: ").strip())
            break
        except ValueError:
            print("Please enter a valid number for price.")

    filter_products_by_price(input_file, output_file, min_price)

