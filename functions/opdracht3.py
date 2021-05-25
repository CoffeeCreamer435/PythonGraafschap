from termcolor import colored

def vierkant(number: int, color: str):
    for i in range(0, number, 1):
        draw(number, color)


def draw(lineLength: int, color: str):
    lineToDraw = ''
    for i in range(0, lineLength, 1):
        lineToDraw += '▮'
    print(colored(lineToDraw, color))

vierkant(5, 'green')