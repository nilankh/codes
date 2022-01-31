'''
    1
   121
  12321
 1234321
123454321

'''



n=int(input())
i=1
while i<=n:
    #spaces sequence
    spaces=1
    while spaces<=n-i:
        print(' ',end='')
        spaces=spaces+1
    #increasing sequence
    p=1
    j=1
    while j<=i:
        print(p,end='')
        j=j+1
        p=p+1
    #decreasing sequences
    p=i-1
    while p>=1:
        print(p,end='')
        p=p-1
    print()
    i=i+1
