
import random

def randstring (length=5):

    valid_word = input( 'enter a valid word: ')

    return ''.join(random.choice(valid_word) for i in range(5))
print (randstring())









