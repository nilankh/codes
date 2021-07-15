def printPairDiffK(li, k):
##  suppose user entered k as an negative number then we will do this
    
    if k < 0:
        k *= -1
    m = {}
    for num in li:
        #print("just for ke neeche num ki value = ", num)
        if num + k in m:
     
            for i in range(0, m[num + k]):
                print(num, num + k)
        if k != 0 and num - k in m:
            for i in range(0, m[num - k]):
                print(num - k, num)

        if num in m:
            #print("if num", num)
            m[num] += 1
            #print("if statement is working", m)
        else:
            #print("else num", num)
            m[num] = 1
            #print("else statement is working", m)
n = int(input())
li = [int(x) for x in input().split()]
k = int(input())
printPairDiffK(li, k)
