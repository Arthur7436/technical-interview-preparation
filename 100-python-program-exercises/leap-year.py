#wrtie a program to check if it is a leap year
x = int(input('year: '))
while x > 0:
    if (x%4) == 0:
        print('This is a leap year')
        break
    else:
        print('This is not a leap year')
        break