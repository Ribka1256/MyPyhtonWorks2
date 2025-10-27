import random
print('Wellcome to the game!')
score = 0
while True:
    
    ch = input('Do you want play this game(enter yes or no): ').lower()
    if ch == 'yes':
        score +=1
        print('you have now started the game....')
        print('You have 10 attempts to guess the number')
        try:
            topOfRange = int(input('Enter the top of your range: '))
            if topOfRange < 1:
                print('Please enter a number greater than 0.')
                
                continue
        except ValueError:
            print('Invalid number. Please enter a valid integer.')
            continue
        
        guessed = random.randint(1, topOfRange)
        attempts = 10
        guessedNum = False
       
        for i in range(attempts):
            while True:
                try:
                    choice = int(input(f'Attempt {i+1}/{attempts} - Enter your guessed number: '))

                    if choice < guessed:
                        print('Too low!')
                    elif choice > guessed:
                        print('Too high')
                    elif choice == guessed:
                        print('You have guessed it right conguratulation')
                        guessedNum = True
                        print(f'You have guessed it in {score} attempt')
                        break
                except ValueError:
                    print('Invalid input! Please enter a number.')
                    
        if not guessedNum:
            print(f'Sorry! The correct number was {guessed}')
            
    def computerGuess(topOfRange):
        low = 1
        high = topOfRange
        feedBack = ''
        while True:
            feedBack != 'c' and low!= high
            guess = random.randint(low, high)
            if feedBack == 'h':
                high = guess - 1
            elif feedBack == 'l':
                low = guess + 1
        print('The computer guessed it right')
#computerGuess(10)
           
            
    elif ch == 'no':
        print('You are now exiting the game!')
        break
    else:
        print('Invalid input! please try again')
        continue
            
    
 computerGuess(10)