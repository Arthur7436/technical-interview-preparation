# write a program to perform add, sub, mult and div on two given matrices
x = [[2,7,3],[4,5,6],[7,8,9]]
y = [[5,8,1],[6,7,3],[4,5,9]]

result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]
for r in result:
    print('Addition:',r)
    
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] - y[i][j]
for r in result:
    print('Subtraction:',r)

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] * y[i][j]
for r in result:
    print('Multiplication:', r)
    
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] / y[i][j]
for r in result:
    print('Divison:',r)

    


