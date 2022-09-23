# Write a program which repeatedly needs numbers until the user enters 'done'. Once 'done' is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

# Code that collects data
count = 0
sum = 0
number_inputted = 0

while True:
    number_inputted = input('Enter number here: ') 
     #Collects number inputted and stores into number_inputted
    if number_inputted == 'done': 
    #When user enters 'done' code prints 'All done' and loop is stopped
        print('All done!') 
        break
    else:
        #If user does not type 'done' and continues to type numbers the loop continues
        # If the value is not a float, then the output becomes 'Invalid input' and loop continues
        try:
            number_inputted = float(number_inputted)
        except:
            print('Invalid input')
            continue
        # section below ensures that the program counts how many times the user as inputted numbers after entering a value
        # 
        count = count + 1
        sum = number_inputted + sum
    
print('Count: ',count,'Total: ',sum,'Average: ',sum/count)

# Calculates data



# Prints out data