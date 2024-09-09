players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("]nMy friend's favorite foods are:")
print(friend_foods)

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'bmw'
car == 'bmw'

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

age=18
age==18

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
age < 21

age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21

age_0 = 22
age_1 = 18
result = age_0 >= 21 and age_1 >= 21
print(result)

requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings


'pepperoni' in requested_toppings
print(result)

game_active = True
can_edit = False

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
if age <= 18:
    print("I'm too young to vote!")
    print("Time to eat dinner!")

age = 13
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("momamia!")

age = 1
if age < 4:
    print("Your admission cost is $0.")
elif age <18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("adding extra cheese.")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

alien_0 = {'color': 'green', 'points':5}

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0 = {'color': 'green', 'points':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}

alien_0['color']= 'green'
alien_0['points'] = 5

print(alien_0)

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

friends = ['phil','sarah']
for name in favourite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in firends:
        language = favorite_languages[name].title()