
#O(n^2)
def findDuplicate(arr):
    length=len(arr)
    for i in range(0,length):
        for j in range(i+1,length):
            if(arr[i]==arr[j]):
                #print(arr[i],end='')
                return arr[i]
    return -1

n=int(input())
arr=[int(x) for x in input().split()]
print(findDuplicate(arr))

'''

def FindDuplicates(arr):
    size=len(arr)
    result=0
    for i in range(0,size-1):
        #result^=i
        result^=i^arr[i]
    return result^arr[size-1]

n=int(input())
arr=[int(x) for x in input().split()]
ans=FindDuplicates(arr)
print(ans)'''
