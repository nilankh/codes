'''
1
11
202
3003
40004
'''

n=int(input())
print(1)
i=1
while i<n:
    j=0
    while j<i+1:
        if(j==0 or j==i):
            print(i,end='')
        else:
            print(0,end='')
        j=j+1
    print()
    i=i+1
'''ye v kr skte h
n=int(input())
print(1)
i=1
while i<=n:
    j=0
    while j<=i:
        if(j==0 or j==i):
            print(i,end='')
        else:
            print(0,end='')
        j=j+1
    print()
    i=i+1
    '''
