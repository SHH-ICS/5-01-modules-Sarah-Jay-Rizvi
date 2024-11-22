# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.
import random
num = random.randint(0,100)
print(num)
num = random.randint(0,100)
print(num)
print('what is the sum of')
input()
if num + num: 
    print('Correct!') 
else:
    print('incorrect')
