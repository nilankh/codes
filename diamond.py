n=int(input())
n1=(n//2+1)
i=1
while i<=n1:
    spaces=1
    while spaces<=n1-i:
        print(' ',end='')
        spaces=spaces+1
    j=1
    while j<=2*i-1:
        print('*',end='')
        j=j+1
    print()
    i=i+1
n2=n-n1
i=n2
while i>=1:
    spaces=1
    while spaces<=n1-i:
        print(' ',end='')
        spaces=spaces+1
    j=1
    while j<=2*i-1:
        print('*',end='')
        j=j+1
    print()
    i=i-1
