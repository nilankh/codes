'''
n = int(input())
for j in range(1, n + 1):
    result = j * j
    if(result == n):
        print(j)
        break
    elif(result > n):
        print(j - 1)
        break
'''

def squareRoot(n):
    ans = 0
    while(ans * ans <= n):
        ans = ans + 1
    ans = ans - 1
    print(ans)

n = int(input())
squareRoot(n)
