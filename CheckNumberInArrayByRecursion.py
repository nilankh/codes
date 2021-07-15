def checkNumber(arr,x):
    if len(arr)==0:
        return False
    if arr[0]==x:
        return True
    return checkNumber(arr[1:],x)
n=int(input())
arr=[int(x) for x in input().split()]
x=int(input())
if checkNumber(arr,x):
    print('true')
else:
    print('false')
