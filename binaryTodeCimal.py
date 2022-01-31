def binaryToDecimal(binary):
    i=0
    s=0
    while(binary):
        s=s+pow(2,i)*(binary%10)
        binary=binary//10
        i=i+1
    return s
binary=int(input())
s=binaryToDecimal(binary)
print(s)
