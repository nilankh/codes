def pairSum(arr):
    for i in range(0,n):
        for j in range(i+1,n):
            if(arr[i]+arr[j] == sum):
                if(arr[i]<arr[j]):
                    print(arr[i]," ",arr[j],sep="")
                else:
                    print(arr[j]," ",arr[i],sep="")

n=int(input())
arr=[int(x) for x in input().split()]
sum=int(input())
pairSum(arr)
'''
def pairSum(arr,x):
    i, j = 0 , n - 1
    while i < j:
        k = arr[i] + arr[j]
        if k < x:
            i = i + 1
        elif k > x:
            j = j - 1
        else:
            k1 = arr[i+1:].count(arr[j])
            #k2 = arr.count(arr[i])
            #k3 = k1 * k2
            while k1  > 0:
                print(arr[i], arr[j])
                k1 = k1 -1
            i = i + 1
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sum=int(input())
#mergeSort(arr,0,n)
x3 = sorted(arr)
pairSum(x3, sum)

'''
