from typing import cast


currentNumber = 0
while True:
    print('Geef getal')
    inputValue = input()
    if (inputValue == 'stop'):
            break
    try:
        currentNumber = currentNumber + float(inputValue)
    except Exception:
        print('Nope dit is geen getal!')
    print(currentNumber)