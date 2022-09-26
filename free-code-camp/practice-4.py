# Calculating the sum of a string of integers

sum = 0
print('Before ', sum)
for number in (1, 58, 69, 4, 7, 6, 56):
    sum = number + sum
    print(sum, number)
print('Sum of numbers: ', sum)

