# write a program to find factorial of any given number (use a while loop)

x = int(input('Enter number: '))
factorial = 1

while x > 1:
    factorial = factorial * x
    x = x - 1
print(factorial)
    