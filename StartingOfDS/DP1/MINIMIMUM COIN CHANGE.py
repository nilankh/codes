#TOP DOWN APPROACH
'''
import sys
def minimumCoinChange(n, coins, dp):

    
    #base case
    if n == 0:
        return 0
    #LOOKUp
    if(dp[n] != 0):
        return dp[n]
    #rec case
    ans = sys.maxsize
    for i in range(0, m):
        if(n - coins[i] >= 0):
            subprob = minimumCoinChange(n - coins[i], coins, dp)
            ans = min(ans, subprob + 1)
    dp[n] = ans
    return dp[n]
        

n = int(input())
coins = [int(c) for c in input().split()]
m = len(coins)
dp = [0 for i in range(n + 1)]
#p[100] = 0

ans = minimumCoinChange(n, coins, dp)
print(ans)
'''
'''
you have given coins you need to make change for certain rs by using minimum no of coins or currency
form the avilable denomination, for each type of coins we can choose infinite coins of same type which means yiu can use same coins
multiple timess, so what is the minimum no of coin needed to make given ceratin rs

'''


#bottom down
import sys
def minimumCoinChange(n, coins):
    dp = [0 for i in range(N + 1)]

    for n in range(1, N + 1):
        dp[n] = sys.maxsize
        for i in range(0, m):
            if(n - coins[i] >= 0):
                sub = dp[n - coins[i]]
                dp[n] = min(dp[n], sub + 1);
    return dp[n]         
                   
        
  

N = int(input())
coins = [int(c) for c in input().split()]
m = len(coins)

#p[100] = 0

ans = minimumCoinChange(N, coins)
print(ans)






