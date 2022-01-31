n=int(input())
li=[int(x) for x in input().split()]
ele_to_be_searched=int(input())
isFound=False
for i in range(len(li)):
    if li[i]==ele_to_be_searched:
        print(i)
        isFound=True
if isFound is False:
    print(-1)
