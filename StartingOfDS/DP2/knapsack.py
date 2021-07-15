#1st way recursion 
'''
def knapsack(W, val, wt, n, i):

    #base case
    if i == n:
        return 0

    if wt[i] > W:
        ans = knapsack(W, val, wt, n, i + 1)

    else:
        #inclusion of ith ite,
        ans1 = val[i] + knapsack(W - wt[i], val, wt, n, i + 1)

        #exclusion of the ith item
        ans2 = knapsack(W, val, wt, n, i + 1)       
        ans = max(ans1, ans2)
    return ans


val = [200, 300, 100]
wt = [20, 25, 30]
W = 50
n = len(val)
ans = knapsack(W, val, wt, n, 0)
print(ans)'''


#2nd way
#overlapping problems in Knapsack
##recursion memoziation shared by student
##def knapsack(value,weight,w,i,n,dp):
##    if i==n:
##        return 0
##    
##    if weight[i]>w:
##        if dp[i+1][w]==-1:
##            ans=knapsack(value,weight,w,i+1,n,dp)
##            dp[i+1][w]=ans
##        else:
##            ans=dp[i+1][w]
##    else:
##        if dp[i+1][w-weight[i]]==-1:
##            small_ans1=knapsack(value,weight,w-weight[i],i+1,n,dp)
##            ans1=value[i]+small_ans1
##            dp[i+1][w-weight[i]]=small_ans1
##        else:
##            ans1=dp[i+1][w-weight[i]]+value[i]
##        if dp[i+1][w]==-1:
##            ans2=knapsack(value,weight,w,i+1,n,dp)
##            dp[i+1][w]=ans2
##        else:
##            ans2=dp[i+1][w]
##        ans=max(ans1,ans2)
##    return ans
##n=int(input())
##weight=[int(ele) for ele in input().split()]
##value=[int(ele1) for ele1 in input().split()]
##w=int(input())
##dp=[[-1 for j in range(w+1)]for i in range (n+1)]
##a=knapsack(value,weight,w,0,n,dp)
##print(a)



#3rd way iterative
##def knapsack(W, val, wt):
##
##    n = len(val)
##    dp = [[0 for j in range(W + 1)] for i in range(n + 1)]
##    print(dp)
##    for i in range(1, n + 1):
##        for j in range(1, W + 1):
##            #print(j)
##
##            if j < wt[i - 1]:
##                ans = dp[i - 1][j]
##            else:
##                ans1 = val[i - 1] + dp[i - 1][j - wt[i - 1]]
##                ans2 = dp[i - 1][j]
##                ans = max(ans1, ans2)
##            dp[i][j] = ans
##    return dp[n][W]
##val = [20,30,40]
##wt = [1,1,1]
##W = 2
###val = [200, 300, 100]
###wt = [20, 25, 30]
###W = 50
##n = len(val)
##ans = knapsack(W, val, wt)
##print(ans)

#boottm up google
def ks(W, wt, val):
    n = len(val)
    if W <= 0 or n == 0 or len(wt) != n:
        return 0
    dp = [[0 for x in range(W+1)] for y in range(n)]
    for i in range(0, n):
        dp[i][0] = 0
    for c in range(0, W + 1):
        if wt[0]<= c:
            dp[0][c] = val[0]
    for i in range(1, n):
        for c in range(1, W + 1):
            p1,p2 = 0, 0
            if wt[i] <= c:
                p1 = val[i] + dp[i - 1][c-wt[i]]
            # exclude kr do item
            p2 = dp[i - 1][c]
            #max le lo
            dp[i][c] = max(p1, p2)
    ## maximum profit will be at the bottom-right corner.
    return dp[n - 1][W]
val = [60, 100, 120]#{profit)
wt = [10,20,30]#{weifhts}
W = 50#capacity
#val = [200, 300, 100]
#wt = [20, 25, 30]
#W = 50
n = len(val)
ans = ks(W, wt,val)
print(ans)







