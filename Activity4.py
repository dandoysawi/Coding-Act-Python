friends = ["Alice", "Bob", "Carol"]
friends.append("Dave")
friends.insert(1, "Eve") # Add Eve at index 1
friends.remove("Eve")    # Remove Eve

# Formatting the list for printing
print(", ".join(friends[:-1]) + ", and " + friends[-1])

friends.sort()
print(f"Sorted list: {friends}")
