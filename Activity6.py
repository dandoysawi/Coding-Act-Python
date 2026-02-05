sentence = input("Enter a sentence: ")

print(f"Upper: {sentence.upper()}")
print(f"Lower: {sentence.lower()}")
print(f"Count of 'a': {sentence.lower().count('a')}")
print(f"Starts with 'Hello': {sentence.startswith('Hello')}")

print("\nWords line by line:")
for word in sentence.split():
    print(word)
