# write a program which performs add, substract, mulitply and divide of two numbers

# allow user to input first number
    
    

num1 = input('Enter the first number: ')   
try:
    num1 = int()
except ValueError:
    print('Invalid number, please try again')
    num1 = input('Enter the first number: ')
    
    
num2 = input('Enter the second number: ')
try:
    num2 = int(num2)
except ValueError:
    print('Invalid number, please try again')
    num2 = input('Enter the second number: ')
# program calculations according to the users inputted numbers

add = int(num1) + int(num2)
sub = int(num1) - int(num2)
multiply = int(num1) * int(num2)
divide = int(num1) / int(num2)


# Calculations output
print('Addition:',add)
print('Subtract:',sub)
print('Muiltiplication:',multiply)
print('Division:',divide)

    
    
    