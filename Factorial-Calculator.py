import math

numbers = []

while True:
    number = input("enter a non-negative natural number, or 'exit': ")
    if number=="exit":
        break
    numbers.append(int(number))

result = list(map(lambda x: math.factorial(x), numbers))
print(result)