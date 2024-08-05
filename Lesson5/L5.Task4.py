
import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
operator = '+'

correct_answer = num1 + num2
user_answer = int(input(f'What is {num1} {operator} {num2}' " " ))
if user_answer == correct_answer:
    print('Correct!')
else:
    print('Incorrect!')
