filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()

except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)

import json

username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")

import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")

def get_formatted_name(first, last):
    full_name = f"{first} {last}"
    return full_name.title()

#def get_formatted_name(first, last):
#    full_name = f"{first} {last}"
#    return full_name.title()

from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")
