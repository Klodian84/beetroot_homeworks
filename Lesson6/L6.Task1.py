# The Greatest number

# import Random
import random

# Create a random empty list.
random_numbers = []
count = 0
# Create a random list of numbers.
while count < 10:
    number = random.randint(1, 100)
    random_numbers.append(number)
    count += 1
# compare and define the largest number in the random list.
largest_number = random_numbers[0]
index = 1

while index < len(random_numbers):
    if random_numbers[index] > largest_number:
        largest_number = random_numbers[index]
    index = index + 1
# Print the List and the largest value.
print("Random Numbers", random_numbers)
print("Largest Number", largest_number)
