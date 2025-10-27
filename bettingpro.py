import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3
 
symbol_count = {
    'A' : 2,
    'B' : 4,
    'C' : 6,
    'D' : 8,
}

symbol_value = {
    'A' : 5,
    'B' : 4,
    'C' : 3,
    'D' : 2,
}

def check_winning(columns, lines, bet, values):
    winning = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winning += values[symbol] * bet
            winning_lines.append(line + 1 )
    return winning, winning_lines

def get_slot_machine(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            values = random.choice(current_symbols)
            current_symbols.remove(values)
            column.append(values)
            
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns) :
            if i != len(columns) - 1:
                print(column[row],end =' | ')
            else:
                print(column[row],end = '')
        print()

def deposit():
    while True:
        amount = input('Enter the amount you would like to palace on the bet($) : ')
        if amount.isdigit() :
            amount = int(amount)
            if amount <= 0 :
                print('Please amount greater than 0')
            else:
                break
        else:
            print('Please enter a number')
    return amount

def get_number_of_line():
    while True:
        lines = input('Enter the number of bet on (1-'+ str(MAX_LINES) + ')? ')
        if lines.isdigit() :
            lines = int(lines)
            if 1<= lines <= MAX_LINES :
                break
            else:
               print('Please bet on with in the range!')
        else:
            print('Please enter a number')
    return lines
def get_bet():
    while True:
        amount = input('Enter the amount you would like to bet on each lines? :$ ')
        if amount.isdigit() :
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
               break
            else:
                print(f'Amount must be between ${MIN_BET} - ${MAX_BET}')
        else:
            print('Please enter a number')
    return amount

def spin(balance):
    lines = get_number_of_line()
    while True :
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f'You do not have enough in your balance{balance}')
        else:
            break
        
    print(f'You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}')
    
    slot = get_slot_machine(ROWS, COLS, symbol_count)
    print_slot_machine(slot)
    winning, winning_lines  = check_winning(slot, lines, bet, symbol_value)
    print(f'You won !${winning}')
    print(f' You won on lines: ', *winning_lines)
    return winning - total_bet

def main():
    balance = deposit()
    while True:
        print(f'current balance is ${balance}')
        answer = input('Please enter the spin and play (q to quit).')
        if answer == 'q':
            break
        balance += spin(balance)
    
    print(f'You are left with ${balance}')
        
    
    
main()



        