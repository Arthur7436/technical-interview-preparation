#rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. 

hrs = input('Enter Hours: ')
rte = input('Enter Rate: ')

try: 
    fhrs = float(hrs)
    frte = float(rte)
    
except:
    print('Error, please enter a numeric input')
    quit()
# finding earnings if 1.5 rate is applied for hours worked over 40hrs
if int(hrs) > 40:
    reg = float(hrs) * float(rte)
    otp = (int(hrs)-40.0)*(float(rte)*1.5)
    total_overtime = float(reg) + float(otp)
    print('Pay:$ ',total_overtime)
    print('Overtime')
else:  
    pay = float(hrs) * float(rte)
    print('Pay:$ ', pay)
    print('Regular')