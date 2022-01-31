'''
11111
0000
111
00
1
'''



n=int(input())
i=1
while i<=n:
    j=1
    while j<=n-i+1:
        if i%2==0:
            print(0,end='')
        else:
            print(1,end='')
        j=j+1
    i=i+1
    print()
