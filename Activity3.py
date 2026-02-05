def collatz(n):
    if n % 2 == 0:
        result = n // 2
    else:
        result = 3 * n + 1
    print(result)
    return result

number = int(input("Enter a number: "))
while number != 1:
    number = collatz(number)
