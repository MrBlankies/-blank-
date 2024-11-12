counter = 0
even = 0
numbers = []
import random 
while counter < 20:
    num = random.randint(1, 100)
    numbers.append(num)
    counter += 1
    if num % 2 == 0:
        even += 1
print("List of random numbers: ", numbers)
print("Even numbers: ", even)