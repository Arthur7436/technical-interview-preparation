# Calculating the average of a string of integers

import sunau
# finding the count, sum and average of the string

count = 0
sum = 0
print('Before ', count, sum)
for number in (1, 58, 69, 4, 7, 6, 56):
    count = count + 1
    sum = sum + number
    print(count, sum, number)
    if number > 20:
        print('Large number!', number)
print('count-sum-average: ',count,sum,sum/count)

