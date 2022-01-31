def linear_search(li,ele):
    #li is the list & ele is the element to be searched
    for i in range(len(li)):
        if li[i]==ele:
            return i
    return -1
n=int(input())
li=[int(x) for x in input().split()]
ele=int(input())
index=linear_search(li,ele)
print(index)
