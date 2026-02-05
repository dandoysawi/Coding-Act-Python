cart = {'apple': 2, 'banana': 5, 'milk': 1}
item = input("Enter item to add: ").lower()

if item in cart:
    cart[item] += 1
else:
    cart[item] = 1

# Printing the cart
print("Your cart contains:")
for item, count in cart.items():
    print(f"- {count} {item}(s)")
