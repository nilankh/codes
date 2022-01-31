def fibo(n):
    i=0
    a=0
    b=1
    while(i<n):
        if(i<=1):
            c=i
        else:
            c=a+b
            a=b
            b=c
        i=i+1
        print(c,end=',')
n=int(input())
fibo(n)
