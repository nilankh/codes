'''
def Multiplication(a,b):
    c=a*b
    return c
a=int(input())
b=int(input())
print(Multiplication(a,b))'''

'''

def Multiplication(a,b):
    if a==1 and b==0:
        return 0
    return a*b
a=int(input())
b=int(input())
print(Multiplication(a,b))
'''

'''
def Multiplication(m,n):
    if m==1 and n==0:
        return 0
    else:
        a=m*(n-1)
        return a+m
m=int(input())
n=int(input())
print(Multiplication(m,n))'''

'''
def Multiplication(m,n):
    if m==1 and n==0:
        return 0
    else:
        #a=m*(n-1)
        return m*(n-1)+m
m=int(input())
n=int(input())
print(Multiplication(m,n))'''

def multiplyNumbers(m,n):
    if m==0 or n==0:
        return 0
    if n>0:
        smallAns=multiplyNumbers(m,n-1)
        return smallAns+m
    else:
        smallAns=multiplyNumbers(m,n+1)
        return smallAns-m

from sys import setrecursionlimit
setrecursionlimit(10000)
m=int(input())
n=int(input())
print(multiplyNumbers(m,n))
