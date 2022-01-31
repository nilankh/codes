'''
ABCDE
ABCDE
ABCDE
ABCDE
ABCDE


n=int(input())
i=1
while i<=n:
    j=1
    while j<=n:
        charP=chr(ord('A')+j-1)
        print(charP,end='')
        j=j+1
    print()
    i=i+1'''

'''
k= int(input())
# 'A' + k -1
x = ord('A')
asciiTarget = x + k - 1
targetChar = chr(asciiTarget)
print(targetChar)'''

n = int(input())
i = 1
while(i <= n):
    j = 1
    start_char = chr(ord('A') + i - 1)
    while(j <= n):
        charP = chr(ord(start_char) + j -1)
        print(charP,end = "")
        j = j + 1
    print()
    i = i + 1
        









        
