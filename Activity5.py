# 1. Create the initial dictionary
cart = {'apple': 2, 'banana': 5, 'milk': 1}

# 2. Get user input
item = input("What would you like to add to your cart? ").lower().strip()

# 3. Logic to update or add the item
if item in cart:
    cart[item] += 1
    print(f"Updated {item} count to {cart[item]}.")
else:
    cart[item] = 1
    print(f"Added {item} to the cart.")

# 4. Format and print the output
# We convert the dictionary items into a list of strings for easy formatting
items_list = [f"{count} {name}{'s' if count > 1 and not name.endswith('s') else ''}" for name, count in cart.items()]

if len(items_list) > 1:
    readable_cart = ", ".join(items_list[:-1]) + ", and " + items_list[-1]
else:
    readable_cart = items_list[0]

print(f"\nYou have {readable_cart}.")
