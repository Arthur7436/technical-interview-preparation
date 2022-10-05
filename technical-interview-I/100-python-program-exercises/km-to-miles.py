# write a program to convert kilometers to miles

x = float(input('Kilometres: '))
y = x/(1.609)
decimal = "{:.2f}".format(y) 
print('Miles: ',decimal)