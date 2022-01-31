''' 12345
    23456
    34567
    45678
    56789'''


n=int(input())
i=1
while i<=n:
    j=1
    start_no=1+i-1
    while j<=n:
        P=(start_no+j-1)
        print(P,end='')
        j=j+1
    print()
    i=i+1
