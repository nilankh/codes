''' N ALWAYS BE A ODD NO
for n=5
* 
 * * 
  * * * 
 * * 
* 


n=int(input())
x=1
while x<=n:
    if x<=int(n/2)+1:
        s=0
        while s<x-1:
            print(' ',end='')
            s=s+1
        g=0
        while g<x:
            print('*',end=' ')
            g=g+1
        print()
    else:
        s=n-x-1
        while s>=0:
            print(' ',end='')
            s=s-1
        g=n-x
        while g>=0:
            print('*',end=' ')
            g=g-1
        print()
    x=x+1'''

n=int(input())
increasing=(n+1)//2
decreasing=n-increasing
i=1
while i<=increasing:
    spaces=1
    while spaces<=i-1:
        print(' ',end='')
        spaces=spaces+1
    j=1
    while j<=i:
        print('* ',end='')
        j=j+1
    print()
    i=i+1
#2nd half ke lia
i=1
while i<=decreasing:
    #2nd half ka spaces bole toa printing spaces 1st row has 2 spaces 2nd row has 1 spaces,so ith will have decreasing-i spaces
    spaces=1
    while spaces<=decreasing-i:
        print(' ',end='')
        spaces=spaces+1
    #printing stars 1st row has 3 star 2nd row has 2,so ith will have decreasing-i+1 stars
    j=1
    while j<=decreasing-i+1:
        print('* ',end='')
        j=j+1
    print()
    i=i+1




























