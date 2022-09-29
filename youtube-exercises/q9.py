# write a program to check whether a number is a prime or not

x = int(input('Enter number: '))
if x == 1  or x == 2 or x == 3:
    print('prime number')
if x > 1:
    for i in range(2,int(x/2)+1):
        if int(x%i) == 0:
            print('composite number')
            break
        else:
            print('prime number')
            break

