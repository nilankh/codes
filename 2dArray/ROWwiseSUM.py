def row_sum(arr):
    sum=0
    for i in range(n):
        
        for j in range(m):
            sum+=arr[i][j]
        print(sum,end=' ')
        
     

s=input().split()
n,m=int(s[0]),int(s[1])
b=input().split()
arr=[[int(b[m*i+j])for j in range(m)]for i in range(n)]
row_sum(arr)

