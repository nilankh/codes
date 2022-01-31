def wavePrint(arr):
    for j in range(m):
        if j % 2 == 0:
            for i in range(n):
                print(li[i][j], end = ' ')
        else:
            for i in range(n - 1, -1, -1):
                print(li[i][j], end = ' ')
str = input().split()
n, m = int(str[0]), int(str[1])
b = str[2:]
li = [[int(b[m * i + j]) for j in range(m)] for i in range(n)]
wavePrint(li)
