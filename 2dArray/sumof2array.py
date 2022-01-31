n = int(input())
matrix = []
for i in range(0, n):
    arr = [int(x) for x in input().split()]
    matrix.append(arr)

sum1 = 0
j = 0
#diagonal
for i in range(0, n):
    sum1 = sum1 + matrix[i][j]
    j = j + 1
##    print("First for loop",sum1)

#second diagonal
j = n - 1
for i in range(0, n):
    sum1 = sum1 + matrix[i][j]
    j = j - 1
##    print("Second for loop", sum1)

#boundaries 
for i in range(1, n - 1):
    sum1 = sum1 + matrix[0][i]
    #print("3rdfor loop 1st sum", sum1)
    sum1 = sum1 + matrix[n - 1][i]
    #print("3rdfor loop 2nd sum", sum1)
    sum1 = sum1 + matrix[i][0]
    #print("3rdfor loop 3rd sum", sum1)
    sum1 = sum1 + matrix[i][n - 1]
    #print("3rdfor loop 4th sum", sum1)
if n % 2 != 0:
    sum1 = sum1 - matrix[int(n/2)][int(n/2)]
    #print("iii", sum1)
print(sum1)
