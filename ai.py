
import random

COLORS = ["R", "G", "B", "Y", "W", "O" ]
TRIES = 10
CODE_LENGHT = 4

def generate_code():
    code = []
    for _ in range(CODE_LENGHT):
        color = random.choice(COLORS)
        code.append(color)
    return code

def guess_code():
    
    while True:
        guess = input('Guess: ').upper().split(' ')
        
        if guess != CODE_LENGHT:
            print(f'you muxr guess {CODE_LENGHT} colors.')
            continue
        for color in guess:
            if color not in COLORS:
                print(f'Imvaild color {color}. Try again')
                break
        else:
            break
    return guess

def check_color(guess, real_code):
    color_count = {}
    correct_pos = 0
    incorrect_pos = 0
    
    for color in real_code:
        if color not in color_count:
            color_count[color] = 0
        color_count[color] += 1
    
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in real_color:
            correct_pos += 1
            color_count[guess_color] += 1
             
    for guess_color, real_color in zip(guess, real_code): 
        if guess_color in color_count and color_count[guess_color] > 0:
            incorrect_pos += 1
            color_count[guess_color] += 1
            
    return correct_pos, incorrect_pos
             
def game():
    print(f'Wellcomre to mastermin you have {TRIES} to guess the code...')
    print('The vaild colors are:', *COLORS)
    
    code = guess_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        if correct_pos == CODE_LENGHT:
            print(f'You guessed the code in {attempts} tries!')
            break
        
        print(f'Correct Position: {correct_pos} | Incorrect position: {incorrect_pos}')
    else:
        print('You ran out of tries, the code was:', *code)
    
    if __name__=='__main__':
        game()
            
     

    
    
    
    

