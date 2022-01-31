'''
ABCD
EFGH
IJKL
MNOP'''

n=6
i=1
p=ord('A')

while i<=4:
    j=1
    
    while j<=n:
        c=chr(p)
        print(c,end='')
        p=p+1
        j=j+1
    print()
    i=i+1
