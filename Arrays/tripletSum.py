def TripletSum(arr):
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if(arr[i]+arr[j]+arr[k]==sum):
                    print(arr[i],arr[j],arr[k])

n=int(input())
arr=[int(x) for x in input().split()]
sum=int(input())
TripletSum(arr)
