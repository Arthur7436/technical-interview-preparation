# use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number


str = 'X-DSPAM-Confidence: 0.8475'
x = str.find(' ')
print(x)
y = str.find('5')
print(y)
number = str[19:]
value = float(number)
print(value)

