def fibo(n):
    if n==1 or n==2:
        return 1
    fib_n_1=fibo(n-1)
    fib_n_2=fibo(n-2)
    output=fibo(n-1)+fibo(n-2)
    return output
n=int(input())
print(fibo(n))
