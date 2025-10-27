def getNumber(n) :
    while True :
        operand  = input ('number ' + str(n) + ':')
        try :
            return float(operand)
        except :
            print ('invalid number , trty again')
x = getNumber(1)
y = getNumber(2)
op= str (input('enter the operator : '))

if op == '+' :
     result = x + y
     print ('the sum is ; ',x+y)
elif op == '-' :
      result = x - y
      print ('the difference is ; ',x-y)
elif op == '%' :
      result = x * y
      print ('the product is ; ',x%y)
elif op == '/' :
      result = x / y
      print ('the quotient is ; ',x/y)
else:
      print ('invalid operator')
     