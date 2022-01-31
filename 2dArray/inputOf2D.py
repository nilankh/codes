##str = input().split()
##n, m = int(str[0]), int(str[1])
##li = [[int(j) for j in input().split()]for i in range(n)]
##print(li)


#same code
'''
n = int(input())
m = int(input())
matrix = []
for i in range(n):
    a = []
    for j in range(m):
        a.append(int(input()))
    matrix.append(a)
print(matrix)
'''

#zagged input
#now need to take m column
n = int(input())
li = [[int(j) for j in input().split()] for i in range(n)]
print(li)













