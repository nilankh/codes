'''  1    2   3    4   5
     11   12  13   14  15
     21   22  23   24  25
     16   17  18   19  20
     6    7    8   9   10
     '''
'''
n=4
i=1
p=1
while i<=n:
    spaces=1
    while spaces<=n-i:
        print(' ',end='')
        spaces=spaces+1
    j=1
    while j<=i:
        print(p,end='')
        p=p+1
        j=j+1
   
    i=i+1
    print()


n=int(input())
if n%2==0:
    x=1
    p=int(n/2)
else:
    x=2
    p=int(n/2)+1

    
for i in range(0,p):
    for k in range(1,n+1):
        print((n*i*2)+k,"", end="")
    print()

for j in range(n-x,0,-2):
    for k in range(1,n+1):
        print((n*j)+k,"", end="")
    print()

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
for i in range(1,n+1,1):
    for j in range(1,i,1):
        print(' ',end='')
    for j in range(i,n+1,1):
        print(j,end='')
    print()
for i in range(1,n):
    for j in range(1,n-i,1):
        print(' ',end='')
    for j in range(n-i,n+1,1):
        print(j,end='')
    print()
'''
'''
n=int(input())
i=1
while i<=n:
    spaces=1
    while spaces<=n-i:
        print(' ',end='')
        spaces=spaces+1
    j=1
    while j<=2*i-1:
        print('*',end='')
        j=j+1
    print()
    i=i+1
i=n
while i>1:
    spaces=1
    while spaces<=n-i+1:
        print(' ',end='')
        spaces=spaces+1
    j=1
    while j<=2*i-1:
        print('*',end='')
        j=j+1
    print()
    i=i-1
'''


n=int(input())
i=1
while i<=n//2+1:
    spaces=1
    while spaces<=n//2+1-i:
        print(' ',end='')
        spaces=spaces+1
    j=1
    while j<=2*i-1:
        print('*',end='')
        j=j+1
    print()
    i=i+1
i=n//2+1
while i>1:
    spaces=1
    while spaces<=n//2-i+2:
        print(' ',end='')
        spaces=spaces+1
    j=1
    while j<=2*(i-1)-1:
        print('*',end='')
        j=j+1
    print()
    i=i-1






























































