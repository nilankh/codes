'''
here you have given array of wines bottles which basically denotes price of wines
in the first year, you can sell wines from extreme left or ends (means first or last)
, you have to sell exactly 1 bottle in one year , price of wines increase every year

yth year = p[i] * y
we need to find out what is the maximum profit we can make by selling all the bottle, if u hvae n number of bottle it
will take n year to sell

'''


'''
#1st method
def profit(wines, i, j, y):
    #Base case
    if i > j:
        return 0

    #Recursive case
    op1 = wines[i] * y + profit(wines, i + 1, j, y + 1)
    op2 = wines[j] * y + profit(wines, i, j - 1,  y + 1)
    return max(op1, op2)

    
    

wines = [int(x) for x in input().split()]
print(profit(wines, 0, len(wines) - 1, 1))
5'''



#2nd method

def profit(wines, i, j, y, dp):
    #Base case
    if i > j:
        return 0
    #Return if dp[i][j]
    if(dp[i][j] != 0):
        return dp[i][j]
        

    #Recursive case
    op1 = wines[i] * y + profit(wines, i + 1, j, y + 1, dp)
    op2 = wines[j] * y + profit(wines, i, j - 1,  y + 1, dp)
    dp[i][j] = max(op1, op2)
    return dp[i][j]
    
n = int(input())
dp = [[0 for i in range(n + 1)]for i in range(n + 1)]
wines = [int(x) for x in input().split()]
print(profit(wines, 0, len(wines) - 1, 1, dp))








