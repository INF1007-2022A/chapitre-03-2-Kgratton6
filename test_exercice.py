
value = 22
twenties = tens = fives = ones = 0
while value != 0:
    if value >= 20:
        twenties += value//20
        value = value%20
    elif value >= 10:
        tens += value
        fives += value//5
        value = value%5
    elif value >= 1:
        ones = value
        value = 0

print(twenties, tens, fives, ones)
print(value)
