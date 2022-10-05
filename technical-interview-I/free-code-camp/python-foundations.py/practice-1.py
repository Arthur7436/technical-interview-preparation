#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours


hrs = input('Enter Hours: ')
rte = input('Enter Rate: ')
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
    