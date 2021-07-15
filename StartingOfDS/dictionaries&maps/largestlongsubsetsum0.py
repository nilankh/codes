
def maxLenZeroSum(arr):

    sumsMap = {}
    maxLen = 0
    sumSoFar = 0
    for i in range(len(arr)):
        sumSoFar += arr[i]
        print("sumsoFar", sumSoFar)
        

        if(arr[i] is 0 and maxLen is 0):
            maxLen = 1
            #print("maxlen", maxLen)

        if sumSoFar is 0:
            maxLen = i + 1
            #print("second",maxLen)

        if sumSoFar in sumsMap:
            #print("if ke andar", sumsMap)
            #print('ith value', i)
            #print("sum so Far",sumSoFar)
            maxLen = max(maxLen, i - sumsMap[sumSoFar])
            #print("max length", maxLen)
            
        else:
            
            sumsMap[sumSoFar] = i
            #print("else",sumsMap)

    return maxLen


#brute force
def maxLenZeroSumm(arr):
    maxLen = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum is 0:
                maxLen = max(maxLen, j - i + 1)
    return maxLen

n = int(input())
arr = [int(x) for x in input().split()]
k = maxLenZeroSum(arr)
print(k)











