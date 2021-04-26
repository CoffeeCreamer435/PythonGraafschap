# Collecting the numbers
print('geef een getal')
numberOne = float(input())
print('geeft getal 2')
numberTwo = float(input())

#calculate the sum
print ('De som is' , numberOne + numberTwo)

#get the product
print ('De product is', numberOne * numberTwo)

#get the quotiënt
try:
    print ('De quotiënt is', numberOne / numberTwo)
except ZeroDivisionError:
    print('HAHA nice try. delen door 0 🤗')