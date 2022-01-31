'''
A
BB
CCC
DDDD'''
n=int(input())
i=1
while i<=n:
    j=1
    while j<i+1:
        #printting jth column
        charP=chr(ord('A')+i-1)
        print(charP,end='')
        j=j+1
    print()
    i=i+1
