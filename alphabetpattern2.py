'''
ABCDEF
BCDEFG
CDEFGH
DEFGHI
EFGHIJ
FGHIJK'''


n=int(input())
i=1
while i<=n:
    j=1
    start_char=chr(ord('A')+i-1)
    while j<=n:
        #printting jth column
        charP=chr(ord(start_char)+j-1)
        print(charP,end='')
        j=j+1
    print()
    i=i+1
