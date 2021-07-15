'''
def CountZeros(n):
    if n == 0:
        return 1
    count=0
    while n!=0:
        r=n%10
        if r==0:
            count=count+1
        n=n//10
    return count
        
n=int(input())
print(CountZeros(n))
'''
'''
def CountZeros(n):
    if n==0:
        return 1
    elif n//10==0:
        return 0
    elif n%10==0:
        return 1+CountZeros(n//10)
    else:
        return CountZeros(n//10)
n= int(input())
print(CountZeros(n))'''

#below code by nehasingla
def countZeros(n):
    if n==0:
        return 0
    smallerNumber=countZeros(n//10)
    LastDigit=n%10
    if LastDigit==0:
        return smallerNumber+1
    else:
        return smallerNumber
n=int(input())
print(countZeros(n))
