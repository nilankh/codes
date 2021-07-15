#overlappin h isme
'''
import sys
def minStepsTo1(n):
    if n == 1:
        return 0
    ans1 = sys.maxsize
    if n % 3 == 0:
        ans1 = minStepsTo1(n // 3)

    ans2 = sys.maxsize
    if n % 2 == 0:
        ans2 = minStepsTo1(n // 2)

    ans3 = minStepsTo1(n - 1)
    
    ans = 1 + min(ans1, ans2, ans3)
    return ans
n = int(input())
ans = minStepsTo1(n)
print(ans)
'''
'''
import sys
def minStepsTo1(n):
    dp = [-1 for i in range(n + 1)]
    dp[0] = 0
    dp[1] = 0
    large = sys.maxsize
    for i in range(2, n + 1):
        a = dp[i - 1]
        b = dp[i // 2] if i % 2== 0 else large
        c = dp[i // 3] if i % 3 == 0 else large
        dp[i] = 1 + min(a,b,c)
    return dp[n]



n=int(input())
print(minStepsTo1(n))'''
import sys
def minStepsTo1(n, dp):
    if n == 1:
        return 0

    ans1 = sys.maxsize
    if n % 3 == 0:
        if dp[n // 3] == -1:
            ans1 = minStepsTo1(n // 3, dp)
            dp[n // 3] = ans1
        else:
            ans1 = dp[n //3]

    ans2 = sys.maxsize
    if n % 2 == 0:
        if dp[n // 2] == -1:
            ans2 = minStepsTo1(n // 2, dp)
            dp[n // 2] = ans2
        else:
            ans2 = dp[n // 2]

    if dp[n - 1] == -1:
        ans3 = minStepsTo1(n - 1, dp)
        dp[n - 1] = ans3 
    else:
        ans3 = dp[n - 1]
    ans = 1 + min(ans1, ans2, ans3)
    return ans
 

n = int(input())
dp = [-1 for i in range(n + 1)]
ans = minStepsTo1(n, dp)
print(ans)





