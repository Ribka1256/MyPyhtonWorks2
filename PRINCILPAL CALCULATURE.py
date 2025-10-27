
print('------------PRINCILPAL CALCULATURE-------------')
MAX_n = 4
MIN_N = 1
while True:
    principle = input('Enter your principle amount: ')
    if principle.isdigit():
        principle = int(principle)
        if principle <= 0:
            print('principle can not be less than or equal to zero')
        else:
            break
    else:
        print('Invalid input')

while True:
    rate = input('Enter the rate: ')
    try:
        rate = float(rate)
        if rate <= 0:
            print('principle can not be less than or equal to zero')
        else:
            break
    except:
        print('Invalid input')
        
while True:
    time = input('Enter the time in years: ')
    if time.isdigit():
        time = int(time)
        if time <= 0:
            print('The interset time can not be less than or equal to zero')
        else:
            break
    else:
        print('Invalid input')
while True:
    n = input('Enter your compound amount: ')
    if n.isdigit():
        n = int(n)
        if MIN_N <= n<= MAX_n:
           break
    else:
        print('Invalid input')
        
def amount():
    amount = principle * pow((1 + rate/n) , time)
    print(f'Balance after {time} years is ${amount}')
am = amount()

import time
the_time = int (input('Enter the time in seconds: '))
for x in range(the_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hour = int(x/ 3600)
    print(f'{hour:02}:{minutes:02}:{seconds:02}')
   
    time.sleep(1)
print('TIME IS UP!')  


