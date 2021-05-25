import random

def throw():
    return random.randrange(1,7)

for i in range(1,11, 1):
    print ('worp ', i ,'van de dobbelsteen', throw())