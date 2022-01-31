'''
1
22
303
4004
50005'''

n=int(input())

i=1
while i<=n:
    j=1
    while j<=i:
        if(j==1 or j==i):
            print(i,end='')
        else:
            print(0,end='')
        j=j+1
    print()
    i=i+1
