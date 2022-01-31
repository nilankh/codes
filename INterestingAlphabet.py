'''
5
45
345
2345
12345

n = int(input())
i = 1
p = n
x = p
while(i <= n):
    j = 1
    while(j <= i):
        print(p,end = "")
        p = p + 1
        j = j + 1
    x = x - 1
    p = x
    print()
    i = i + 1
'''

'''
E
DE
CDE
BCDE
ABCDE'''

n = int(input())
i = 1
while(i <= n):
    j = 1
    while(j <= i):
        print(chr(ord('A') + n - i + j),end = "")
        j = j + 1

    print()
    i = i + 1



'''

n = int(input())
i = 1
while(i <= n):
    spaces = 1
    while(spaces <= n - i):
        print(" ",end = "")
        spaces = spaces + 1

    num = 1
    while(num <= i):
        print(num, end = "")
        num = num + 1
    dec = i - 1
    while(dec >= 1):
        print(dec,end = "")
        dec = dec - 1
    print()
    i = i + 1
#another [pattern'''

















