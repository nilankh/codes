def isSortedBetter(a,si):
    length=len(a)
    if si==length-1 or si==length:
        return True
    if a[si]>a[si + 1]:
        return False
    isSmallerPartSorted=isSortedBetter(a,si+1)
    return isSmallerPartSorted
a=[1,2,3,40,5]
print(isSortedBetter(a,0))
'''if isSortedBetter(a,0):
    print('true')
else:
    print('false')'''
