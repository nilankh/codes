def GeometricSum(n):
    if n<0:
        return 0
    return 1/pow(2,n)+GeometricSum(n-1)
n=int(input())
ans=GeometricSum(n)
print(ans)
print("{0:.5f}".format(ans))
