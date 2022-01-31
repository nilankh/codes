'''
1 2 3 4 5 
11 12 13 14 15 
21 22 23 24 25 
16 17 18 19 20 
6 7 8 9 10
'''

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
