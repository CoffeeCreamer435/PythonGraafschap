import random
amountOfSixes = 0


def throw():
    return random.randrange(1, 7)


for i in range(0, 100, 1):
    if throw() == 6:
        amountOfSixes += 1
        
print('Er is 100× gegooid met een dobbelsteen. Het aantal zessen is ', amountOfSixes)
