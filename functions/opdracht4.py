from turtle import *

color('green')

lineLength = 200
bgcolor('pink')
speed(500)
for i in range(0, 200, 1):
    forward(lineLength)
    right(90)
    lineLength -= 1
    
done()