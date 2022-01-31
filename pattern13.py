'''
1        1
12      21
123    321
1234  4321
1234554321
'''



n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end='')
        j=j+1
    spaces=1    
    while spaces<=2*n-2*i:
        print(' ',end='')
        spaces=spaces+1
    j=i
    while j>0:
        print(j,end='')
        j=j-1
    i=i+1
    print()
