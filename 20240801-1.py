from random import randint
randint(1, 6)

from random import choice
players = ['charles', 'artina', 'michael', 'florence', 'eli']
first_up = choice(players)

with open('pi_digits.txt') as file_object:
    contents = file_object.read()

print(contents)

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)