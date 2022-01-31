def PairWithDiff(arr):
    l = len(arr)
    for i in range(l):
        for j in range(1, l):
            if(arr[j] - arr[i] == n):
                print(arr[i]," ", arr[j])
    else:
        print("No Such Pair")

##n = int(input())
##arr = [int(x) for x in input().split()]
##PairWithDiff(arr)





def findPair(arr, n):
    size = len(arr)
    i, j = 0, 1
    while i < size and j < size:
        if i != j and arr[j] - arr[i] == n:
            print(arr[i]," ", arr[j])
            return True
        elif arr[j] - arr[i] < n:
            j += 1
        else:
            i += 1

    print("no Pair found")
    return False
n = int(input())
arr = [int(x) for x in input().split()]
findPair(arr, n)






