'''
   1
  23
 456
78910
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
        print(p   ,end='')
        p=p+1
        j=j+1
   
    i=i+1
    print()
