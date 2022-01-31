'''
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 21 
22 23 24 25 26 27 28 
'''

n=int(input())
i=1
p=1
while i<=n:
    j=1
    while j<=i:
        print(p,end=' ')
        p=p+1
        j=j+1
    print()
    i=i+1
