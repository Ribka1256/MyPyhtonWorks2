import random
def computerGuess(topOfRange):
    low = 1
    high = topOfRange
    feedBack = ''
    while feedBack != 'c':
        if  low!= high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedBack = input(f'is {guess} too high or too low, or correct(c)? ')
        if feedBack == 'h':
            high = guess - 1
        elif feedBack == 'l':
            low = guess + 1
    print('The computer guessed it right')
computerGuess(10)