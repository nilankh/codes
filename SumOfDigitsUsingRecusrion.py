'''
def SumOfDigits(n):
    s=0
    while n>0:
        r=n%10
        s=s+r
        n=n//10
    return s
n=int(input())
print(SumOfDigits(n))'''

def SumOfDigits(n):
    if n==0:
        return 0
    '''else:
        r=n%10
        return r+SumOfDigits(n//10)'''
    return (n%10+SumOfDigits(n//10))

n=int(input())
print(SumOfDigits(n))
