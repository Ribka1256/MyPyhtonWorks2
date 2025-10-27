print('--------CALCULATUR---------')
def getNum(prompt):
    while True:
        val = input(prompt)
        try:
            return float(val)  # allows decimals and negatives
        except ValueError:
            print('Invalid input. Try again.')

x = getNum('Number 1: ')
y = getNum('Number 2: ')
def add(x, y):
  s= x + y
  print (f'the sum is: {s}')
def mius(x, y):
  mi = x - y
  print (f'the difference is: {mi}')
    
def divi(x, y):
  d = x / y
  print (f'the quotient is: {d} ')

def mul(x, y):
  r = x * y
  print (f'the product is: {r} ')
  
def mo(x, y):
  m = x % y
  print (f'the modulo is: {m} ')

while True:  
  print('Select one of them')
  print('1, Addition')
  print('2, Subtraction')
  print('3, Division')
  print('4, Multiplication')
  print('5, Modulo')
  ch = input('Enter your choice(1/2/3/4/5 or q to exit): ') 
  
  if ch == '1' :
    add(x, y)
    
  elif ch == '2' :
    mius(x, y)
    
  elif ch == '3' :
    divi(x, y)
  
  elif ch == '4' :
    mul(x, y)
  
  elif ch == '5' :
    mo(x, y)
  
  elif ch == 'q':
    print('quit') 
    break
  else:
    print ('invalid input')

