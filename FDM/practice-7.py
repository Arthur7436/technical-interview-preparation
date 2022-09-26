# finding the smallest number in a string
smallest_so_far = 100
print ('before ' , smallest_so_far)
for the_num in (1, 58, 69, 4, 7, 6, 56, -1000):
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
    
print ('after ', smallest_so_far)
    