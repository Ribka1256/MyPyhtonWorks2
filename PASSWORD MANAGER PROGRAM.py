
print('----------PASSWORD MANAGER PROGRAM-----------')
pwd = input('Enter your master password: ').lower()
REAL_MASTER = "admin"
if pwd != REAL_MASTER:
    print("Wrong master password! Exiting.")
    exit()
passwords = []
try:
    with open('Password.txt', 'r') as f:
        for line in f:
            account, passw = line.strip().split('-')
            passwords.append({'account': account, 'pwd': passw})
except FileNotFoundError:
    open('Password.txt', 'w').close()  # create the file if not found

def add():
    print('You are now adding new password to your preexiting one...')
    Account = input('Enter the account name: ')
    mode = input('Password: ')
    with open ('Password.txt', 'a') as f:
        f.write(Account + '-' + mode + '\n')
    passwords.append({'pwd': mode})
    print('Password added successfully!\n')

def display():
    print('Displaying the passwords')
    if not passwords:
        print('No passwords stored yet.\n')
    else:
        for entry in passwords:
            print('user:', entry['account'], ', passw:', entry['pwd'])
   
   
while True:
    ch = input('Do you want to display the passwords or add a new one or q for exiting the program: ').lower()
    if ch == 'q':
        break
    if ch == 'display':
        display()
    elif ch == 'add':
        add()
    elif ch == 'q':
     
        break
    else:
        print('Invalid input try again')

