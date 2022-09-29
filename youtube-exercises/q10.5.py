# write a program to find factorial of any given number (use a for loop)

x = int(input('Enter number: '))

for i in range(1, x):
    x = x * i
print(x)    