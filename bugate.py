def accept():
    while True:
        print('Wellcome to the Budget App ')
        Budget = input('Please enter your initial budget : ')
        
        if Budget.isdigit() :
            Budget = int(Budget)
            if Budget <= 0 :
                print('Please amount greater than 0')
            else:
                break
        else:
            print('Please enter a number')
    return Budget
Budget = accept()
expense = []
def add_expense():
    while True:
        description = input('Enter expense description : ')
        if description == "":
            print('Please enter an valid description of expenses')
        else:
            break
    while True:
        amount = input('Enter expense amount : ')
        if amount.isdigit():
            amount = int(amount)
            if amount <= 0:
                print('Please enter a number grater than 0 ')
            else:
                break
    expense.append({'description': description,'amount':amount})
    print(f'Added expense:{description}, Amount: {amount}')
    

def show_budget():
    total_expense = sum(item['amount'] for item in expense)
    remaining = Budget - total_expense
    print(f'Total Expenses: {total_expense}')
    print(f'Remaining Budget: {remaining}')
    print('\nExpense List:')
    for idx, item in enumerate(expense, 1):
        print(f"{idx}. {item['description']} - ${item['amount']}")
            
def main():
    #Budget = accept()
    while True:

        print('What would like you like to do? ')
        print('1, Add an expense')
        print('2, Show budget details')
        print('3, Exit')

        choice = input('Enter your choice(1/2/3): ')
        if choice == '1':
            add_expense()
        elif choice == '2':
            show_budget()
        elif choice == '3':
            print('You are now exiting the program! Thank you for using it')
            break
        else :
            print('Invalid input')
        

  
  
main()  



