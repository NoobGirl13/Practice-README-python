number = int(input("enter the number: "))
print("number: ", number)

print("is positive or negative: ")
if number>0:
    print("positive number")
elif number<0:
    print("negative number")
else:
    print("zero")

print("is odd number or even number: ")
if number%2==0:
    print("even number")
else:
    print("odd number")

import math
print("the root: ", math.sqrt(number))