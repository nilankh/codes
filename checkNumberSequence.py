n = int(input())
a = list(int(i) for i in input().split())
i= 0
#Check for Increasing
while(i + 1 < n and a[i] > a[i + 1]):
    i += 1

#Check for Decreasing
while(i + 1 < n and a[i] < a[i + 1]):
    i +=1

if( i == n -1):
    print("true")
else:
    print("false")

