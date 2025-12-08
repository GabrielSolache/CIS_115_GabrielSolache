# Define a list of products, each represented as a dictionary.
# Each product has an id, name, and price.
PRODUCTS = [
    {"id": 1, "name": "USB Drive (128 GB)", "price": 12.00},
    {"id": 2, "name": "Mac Book Pro (15 inch)", "price": 2900.00},
    {"id": 3, "name": "Arduino 1010", "price": 48.00},
    {"id": 4, "name": "Ring Camera", "price": 156.00},
    {"id": 5, "name": "Smart TV (TCL 70 inch)", "price": 359.00},
]

def show_products():
    """
    Display all products to the user.
    """
    print("\nProduct Catalog:")
    for product in PRODUCTS:
        # Use f-string to neatly print product details
        print(f"{product['id']}. {product['name']} - ${product['price']}")
        
def main():
    # Shopping cart stored as a list of dictionaries
    cart = []
    # Show available products
    show_products()
    # Loop to allow user to select products
    while True:
        prod_id = input("Enter product ID to add to cart (or 'done' to finish): ")
        # Allow user to exit product selection
        if prod_id.lower() == 'done':
            break
        # Validate numeric input for product ID
        if not prod_id.isdigit():
            print("Please enter a valid number.")
            continue
        # Convert ID to integer
        prod_id = int(prod_id)
        # Search for a matching product
        product = next((p for p in PRODUCTS if p['id'] == prod_id), None)
        # If no product with that ID was found
        if not product:
            print("Product not found.")
            continue
        # Ask user for quantity of this product
        qty = input(f"How many '{product['name']}'? ")
        # Validate quantity input
        if not qty.isdigit() or int(qty) <= 0:
            print("Please enter a valid quantity.")
            continue  # Prevent adding invalid quantity
        # Add product & quantity to the cart
        cart.append({"product": product, "qty": int(qty)})
        print(f"Added {qty} x {product['name']} to cart.")
    # If the user added nothing, end program
    if not cart:
        print("Your cart is empty. Goodbye!")
        return
    # Checkout information
    print("\nCheckout")
    name = input("Your Name: ")
    address = input("Address: ")
    # Payment details
    print("\nPayment Information")
    cc_number = input("Credit Card Number: ")
    cc_expiry = input("Expiration Date (MM/YY): ")
    cc_cvv = input("CVV: ")

    # Print invoice
    print("\n--- Invoice ---")
    print(f"Name: {name}")
    print(f"Address: {address}")
    total = 0  # Running total for order
    # Loop through all cart items and calculate totals
    for item in cart:
        line_total = item["product"]["price"] * item["qty"]
        print(
            f"{item['qty']} x {item['product']['name']} "
            f"@ ${item['product']['price']:.2f} each = ${line_total:.2f}"
        )
        total += line_total  # Add each line's total to full total
    print(f"\nTotal: ${total:.2f}")
    # Only display last 4 digits of credit card
    print("\nPayment Method:")
    print(f"Card ending in {cc_number[-4:]}, Exp: {cc_expiry}")
    print("\nThank you for shopping!")
# Start the program
if __name__ == "__main__":
    main()