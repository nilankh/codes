'''

    1
   21
  321
 4321
54321
'''
n=int(input())
i=1
while i<=n:
    spaces=1
    while spaces<=n-i:
        print(' ',end='')
        spaces=spaces+1
    j=i
    while j>0:
        print(j,end='')
        j=j-1
    print()
    i=i+1
