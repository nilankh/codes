'''def fibo(n):
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
        print(c)



def isPrime(n):
    for d in range(2,n):
        if(n % d == 0):
            break
    else:
        return True
    return False
def primeFrom2toN(n):
    for k in range(2, n + 1):
        is_k_prime=isPrime(k)
        if(is_k_prime):
            print(k)
n=int(input("ENTER THE NO:"))
if(n%2==1):
    fibo(int(n//2)+1)
else:
    isPrime(int(n//2))'''



'''
def check_prime(n):
    if n == 2:
        return True
    elif n%2 == 0:
        return False
    end = int(n**(0.5))
    for i in range(3,end+1,2):
        if n%i == 0:
            return False

    return True
      
n = int(input())
result_arr = [0 for i in range(n)]
# odd indices are for fibonacci series
# even indices is for prime no.
result_arr[0] = 1 # first fib no.
result_arr[1] = 2 # first prime no.
result_arr[2] = 1 # second fib no.
result_arr[3] = 3 # second prime no.


for i in range(4,n):
    if i%2 == 0:
        result_arr[i] = result_arr[i-2] + result_arr[i-4]
    else:
        temp = result_arr[i-2] +2
        while True:
            if check_prime(temp):
                result_arr[i] = temp
                break
            else:
                temp += 2

print(*result_arr)'''

def check_prime(n):
    if n == 2:
        return True
    elif n%2 == 0:
        return False
    end = int(n**(0.5))
    for i in range(3,end+1,2):
        if n%i == 0:
            return False

    return True
        
n = int(input())
result_arr = [0 for i in range(n)]
# odd indices are for fibonacci series
# even indices is for prime no.
result_arr[0] = 1 # first fib no.
result_arr[1] = 2 # first prime no.
result_arr[2] = 1 # second fib no.
result_arr[3] = 3 # second prime no.


for i in range(4,n):
    if i%2 == 0:
        result_arr[i] = result_arr[i-2] + result_arr[i-4]
    else:
        temp = result_arr[i-2] +2
        while True:
            if check_prime(temp):
                result_arr[i] = temp
                break
            else:
                temp += 2

ans = result_arr[n-1]
print(ans)
