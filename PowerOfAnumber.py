'''
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input())
exp=int(input())
print(power(base,exp))'''

'''
l=input().split()
base,n=(int(i)for i in l)
result=1
for i in range(0,n):
    result*=base
print(result)
'''

'''
m, n=(int(i) for i in input().strip().split(' '))
def pow(m,n):
    if n==0:
        return 1
    else:
        return (m*pow(m,n-1))
print(pow(m,n))'''


#optimal solution of Power
#with less time & space complexity
x,n=(int(k) for k in input().split())
def Power(x,n):
    if n==0:
        return 1
    Small_power=Power(x,n//2)
    if n % 2 == 0:
        return Small_power*Small_power
    else:
        return x*Small_power
print(pow(x,n))
