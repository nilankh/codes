'''
    1
   12
  123
 1234
12345
'''
n=int(input())
i=1
while i<=n:
    spaces=1
    while spaces<=n-i:
        print(' ',end='')
        spaces=spaces+1
    j=1
    while j<=i:
        print(j,end='')
        j=j+1
    print()
    i=i+1
    
