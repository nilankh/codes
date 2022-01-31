def mergeTwoSortedArrays(arr1,arr2):
    i = 0
    j = 0
    len1 = len(arr1)
    len2 = len(arr2)

    arr = []

    while((i < len1) and (j < len2)):
        if(arr1[i] < arr2[j]):
            arr.append(arr1[i])
            i = i + 1
        else:
            arr.append(arr2[j])
            j = j + 1
    while(i<len1):
        arr.append(arr1[i])
        i = i + 1

    while(j < len2):
        arr.append(arr2[j])
        j = j + 1
    return arr

n1=int(input("ENTER SIZE OF ARR1:"))
arr1=[int(x) for x in input().split()]

n2=int(input("ENTER SIZE OF ARR2:"))
arr2=[int(x) for x in input().split()]

arr=mergeTwoSortedArrays(arr1,arr2)
print(*arr)
