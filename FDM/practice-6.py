# True and False statements
found = False
print ('before', found)
for value in (1, 58, 69, 4, 7, 6, 56):
    if value == 58 :
        found = True
        if found == 58 :
            print ('The number you have been looking for is: ', found)
            
    print(value, found)
print('After ', found)