# 1. Ask for user input
sentence = input("Enter a sentence: ")

# 2. Uppercase and Lowercase
print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")

# 3. Count occurrences of "a"
# Note: .lower() ensures we count both 'A' and 'a'
count_a = sentence.lower().count('a')
print(f"The letter 'a' appears {count_a} times.")

# 4. Check if it starts with "Hello"
if sentence.startswith("Hello"):
    print("The sentence starts with 'Hello'.")
else:
    print("The sentence does not start with 'Hello'.")

# 5. Split into words and print one per line
print("\nWords in your sentence:")
words = sentence.split() # Splits by whitespace by default
for word in words:
    print(word)
