
import random
import time
OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 20
TOTAL_QUESTION = 7

def make_problems():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    exp = str(left) + ' ' +  operator +" " +  str(right)
    answer = eval(exp)
    return exp, answer

wrong = 0
input('press enter to start!')

start_time = time.time()
for i in range(TOTAL_QUESTION):
    exp, answer = make_problems() 
    while True:
        try:
            guess = input('Problem #' + str(i + 1) + ': ' + exp + ' = ' )
            if guess == str(answer):
                print('Correct')
                break
            else:
                print('Wrong')
                wrong += 1
        except:
            print('Invalid input')
        
end_time = time.time()
total_time = end_time - start_time
print('Nice work! you have finished in', total_time, 'seconds')