import random

amountOfOnes = 0
amountOfTwos = 0
amountOfThrees = 0
amountOfFours = 0
amountOfFives = 0
amountOfSixes = 0


def throw():
    return random.randrange(1, 7)

def countValues(value: int):
    global amountOfOnes, amountOfTwos, amountOfThrees, amountOfFours, amountOfFives, amountOfSixes
    if (value == 1):
        amountOfOnes += 1
    elif (value == 2):
        amountOfTwos += 1
    elif (value == 3):
        amountOfThrees += 1
    elif (value == 4):
        amountOfFours += 1
    elif (value == 5):
        amountOfFives += 1
    elif (value == 6):
        amountOfSixes += 1
    

print('Hoe vaak wil je gooien?')
amountOfTrows = int(input())

for i in range(0, amountOfTrows, 1):
    countValues(throw())
   
   
print('aantal keer 1 ', amountOfOnes)
print('aantal keer 2 ', amountOfTwos)
print('aantal keer 3 ', amountOfThrees)
print('aantal keer 4 ', amountOfFours)
print('aantal keer 5 ', amountOfFives)
print('aantal keer 6 ', amountOfSixes)
