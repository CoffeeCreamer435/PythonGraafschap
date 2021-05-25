#GARBAGE CODE NOW. Opdracht van de school 🤮
def main():

    import random, sys
    print('Hello, what is your name?')
    name = input()

    print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
    secretNumber = random.randint(1,20)

    for guessesTaken in range(1, 7):
        print('Take a guess.')
        guess = int(input())

        if guess < 0:
            print('That number is less than 1. Pick another.')
        if guess < secretNumber:
            print('Your guess was too low.')
        if guess > 20:
            print('That number is more than 20. Pick another.')
        if guess > secretNumber:
            print('Your guess was too high.')
        else:
            break

    def restart():
        print('Do you want to play again?')
        print('Press y to continue. Press n to quit.')
        
    if guessesTaken == 1:
            print('Wow, ' + name + '! You got it in the first try.')
            restart()
    if guess == secretNumber:
        print('Congratulations, ' + name + '! You made it in ' + str(guessesTaken) + ' guesses!')
        restart()
    if guss != secretNumber:
        print('Nope, the number I was thinking of was ' + str(secretNumber) + '.')
        restart()

    while True:
        while True:
            answer = input()
            if answer in ('y', 'n'):
                break
            print('Invalid input.')
        if answer == 'y':
            main()
        else:
            print('Goodbye.')
            sys.exit()
main()