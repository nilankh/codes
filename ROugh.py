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
n=int(input())
print(CountZeros(n))

def CountZeros(n):
    if n==0:
        return 0
    smaller=CountZeros(n//10)
    LastDigit=n%10
    if LastDigit==0:
        return smaller+1
    else:
        return smaller

n=int(input())
print(CountZeros(n))'''
def StringToInteger(n):
    if len(n)==0:
        return 0
    if len(n)==1:
        return int(n[0])
    else:
        return int(n[-1])+10*StringToInteger(n[:-1])
n=input()
print(StringToInteger(n))
