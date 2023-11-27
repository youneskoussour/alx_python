#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print("Please enter a number between -10 and +10",number)
if number>0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")



