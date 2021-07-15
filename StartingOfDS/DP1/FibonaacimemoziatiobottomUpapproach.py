'''
def fibb(n):
    dp = [0 for i in range(n + 1)]
    #print(dp)    
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[n]
n = int(input())


ans = fibb(n)
print(ans)'''
#space O(n) time O(N)


#avi space O(1) kr rhe h

def fibb(n):
    if(n == 0 or n == 1):
        return n
    a = 0
    b = 1
    
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return c
n = int(input())
ans = fibb(n)
print(ans)
