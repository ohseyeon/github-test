pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese'],}

print(f"You ordered a {pizza['crust']}-crust pizza" "with the following topping:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

users = {'aeinstein': {'first': 'albert', 'last': 'einstein', 'location': 'princeton'},
         'mcurie': {'first': 'marie', 'last': 'curie', 'location': 'paris',},}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

#current_number = 1
#while current_number <= 5:
#    print(current_number)
#   current_number += 1

#prompt = "\nTell me something and I will repeat it back to you:"
#rompt += "\nEnter 'quit' to end the program."
#message = ""
#while message != 'quit':
#    message = input(prompt)

#    if message != 'quit':
#        print(message)

#prompt = "\nTell me something, and I will repeat it back to you:"
#prompt += "\nEnter 'quit' to end the program."

#active = True
#while active:
#    message = input(prompt)

#    if message == 'quit':
#        active = False
#    else:
#        print(message)

#prompt = "\please enter the name of a city you have visited:"
#prompt += "\n(Enter 'quit' when you are finished.)"

#while True:
#    city = input(prompt)

#    if city == 'quit':
#        break
#    else:
#        print(f"I'd love to go to {city.title()}!")

unconfirmed_users = ['alice', 'brain', 'Candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

def greet_user(username):
    print(f"Hello, {username.title()}!")

greet_user('Sarah')

def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

def describe_pet(pet_name, animal_type= 'dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie')

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(size, *toppings):
    print("f\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#def make_pizza(size, *toppings):
#    print(f"\nMaking a {size}-inch pizza with the following toppings:")
#    for topping in toppings:
#        print("- " + topping)

#from pizza import make_pizza as mp
#mp(16, 'pepperoni')
#mp(12, 'mushrooms', 'green peppers', 'extra cheese')

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
