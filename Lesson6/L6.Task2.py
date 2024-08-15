# Exclusive common numbers.

import random

random_numbers1 = []
random_numbers2 = []
uniques = []
counter = 0

while counter < 10:
    random_numbers1.append(random.randint(1, 100))
    random_numbers2.append(random.randint(1, 100))
    counter += 1
    print(random_numbers1, random_numbers2)

for number in random_numbers1 and random_numbers2:
    if number not in uniques:
        uniques.append(number)
        print(uniques)
