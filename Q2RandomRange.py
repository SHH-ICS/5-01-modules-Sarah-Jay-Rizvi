# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.
from random import randint

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

if start <= end:
    print("Random number:", randint(start, end))
else:
    print("Invalid range.")
