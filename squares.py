squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

squares = [value ** 2 for value in range(1, 11)]
print(squares)

squares = [value ** 2 for value in range(1, 1001)]
print(squares)

odd_numbers = list(range(1,20,2))
print((odd_numbers))

third = []
for value in range(1, 31):
    third.append(value*3)

print(third)

triple = [value ** 3 for value in range(1, 11)]
print(triple)