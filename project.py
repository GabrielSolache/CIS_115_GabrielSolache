# Define a list of products, each as a dictionary with id, name, and price.
PRODUCTS = [
    {"id": 1, "name": "USB Drive (128 GB)", "price": 12.00},
    {"id": 2, "name": "Mac Book Pro (15 inch)", "price": 2900.00},
    {"id": 3, "name": "Arduino 1010", "price": 48.00},
    {"id": 4, "name": "Ring Camera", "price": 156.00},
    {"id": 5, "name": "Smart TV (TCL 70 inch)", "price": 359.00},
]

def show_products():
    # Display all products in the catalog.
    print("\nProduct Catalog:")
    for product in PRODUCTS:
        print(f"{product['id']}. {product['name']} - ${product['price']}")

def main():
    cart = []  # Create an empty shopping cart (list).

    show_products()  # Show the product catalog to the user.

    # Start a loop to let the user add products to their cart.
    while True:
        prod_id = input("Enter product ID to add to cart (or 'done' to finish): ")
        if prod_id.lower() == 'done':  #  If user types 'done', exit the loop.
            break
        if not prod_id.isdigit():      # Check if input is a number.
            print("Please enter a valid number.")
            continue
        prod_id = int(prod_id)         # Convert input to integer.
        # Find the product by its ID.
        product = next((p for p in PRODUCTS if p['id'] == prod_id), None)
        if not product:                # If product not found, ask again.
            print("Product not found.")
            continue
        qty = input(f"How many '{product['name']}'? ")  # Ask for quantity.
        if not qty.isdigit() or int(qty) <= 0:           # Validate quantity.
            print("Please enter a valid quantity.")
        #  Add the selected product and quantity to the cart.
        cart.append({"product": product, "qty": int(qty)})
        print(f"Added {qty} x {product['name']} to cart.")

    if not cart:  # If cart is empty, end program.
        print("Your cart is empty. Goodbye!")
        return

    # Collect user's name and address for shipping.
    print("\nCheckout")
    name = input("Your Name: ")
    address = input("Address: ")

    # Collect credit card information for payment.
    print("\nPayment Information")
    cc_number = input("Credit Card Number: ")
    cc_expiry = input("Expiration Date (MM/YY): ")
    cc_cvv = input("CVV: ")

    # Print invoice
    print("\n--- Invoice ---")
    print(f"Name: {name}")
    print(f"Address: {address}")
    total = 0 