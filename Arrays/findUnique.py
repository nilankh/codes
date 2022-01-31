def findUnique(arr):
    length=len(arr)
    for i in range(0,length):
        for j in range(0,length):
            if(arr[i] == arr[j] and i!=j):
                break
        else:
            return arr[i]
    #return arr[length-1]
    return -1

n=int(input())
arr=[int(x) for x in input().split()]
number=findUnique(arr)
print(number)

#timecomplexity O(n^2)
'''
def findUnique(arr):
    length=len(arr)
    for i in range(0,length):
        for j in range(0,length):
            if(arr[i]==arr[j] and i!=j):
                break
        else:
            print( arr[i])

n=int(input())
arr=[int(x) for x in input().split()]
findUnique(arr)
#print(number)'''

"""
def findUnique(arr):
    length=len(arr)
    res=arr[0]
    for i in range(1,length):
        res=res^arr[i]
    return res
n=int(input())
arr=[int(x) for x in input().split()]
print(findUnique(arr))"""
