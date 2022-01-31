def sumOfArrays(arr1,arr2):
    i=len(arr1)-1
    j=len(arr2)-1
    R=[]
    carry=0
    while i>=0 and j>=0:
        sum=arr1[i]+arr2[j]+carry
        carry=sum//10
        R.append(sum%10)
        i-=1
        j-=1
        
    while i>=0:
        sum=arr1[i]+carry
        carry=sum//10
        R.append(sum%10)
        i-=1
    while j>=0:
        sum=arr2[j]+carry
        carry=sum//10
        R.append(sum%10)
        j-=1
    R.append(carry)
    R.reverse()

    return R


n1=int(input())
arr1=[int(x) for x in input().split()]
n2=int(input())
arr2=[int(x) for x in input().split()]
R=sumOfArrays(arr1,arr2)
print(*R)
