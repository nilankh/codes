def Fibonacci(n): 
    a=0
    b=1
    c=a+b
    while c<n:
        a=b
        b=c
        c=a+b
    if c==n:
        return(1)
    else:
        return(0)
n=int(input())
if(Fibonacci(n)):
    print("true")
else:
    print("false")
