'''
a=0
b=1
n=int(input("ENTER NO OF FIBONACCI TO BE GENERATED:"))
if n<=0:
    print("Not Possible")
elif n==1:
    print(a)
elif n>=2:
    print("{},{}".format(a,b),end='')
    for i in range(2,n):
        c=a+b
        print(",{}".format(c),end='')
        a=c
        b=c'''

N = int(input())


i = 0
a = 0
b = 1
while(i < N):
    if(i <= 1):
        c = i
    else:
        c = a+b
        a=b
        b=c
           
    i = i + 1

    
    print(c,end=",")





    
