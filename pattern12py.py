'''o/p
1
11
121
1221
'''

n=int(input())
i=0
while i<n:
    j=0
    while j<i+1 :
        if(j==0 or j==i):
            print(1,end='')
        else:
            print(2,end='')
        j=j+1
    i=i+1
    print()
'''
n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        if(j==1 or j==i):
            print(1,end='')
        else:
            print(2,end='')
        j=j+1
    print()
    i=i+1
ye v chalega'''
