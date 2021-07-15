def SubsetArray(arr):
    n = len(arr)
    if n <= 0:
        output = [list()]
        return output
    smallerOutput = SubsetArray(arr[1:])
    return smallerOutput + [[arr[0]] + b for b in smallerOutput]

    

n = int(input())
arr = [int(c) for c in input().split()]
output = SubsetArray(arr)
for lst in output:
    for num in lst:
        print(num, end = ' ')
    print()










##copied by student
##def subset(arr):
##    n = len(arr)
##    if n <= 0:
##        output = [ [] ]
##        return output
##    
##    output = subset(arr[:n-1])
##    outputLen = len(output)
##    
##    for i in range(outputLen):
##        output.append(output[i].copy())
##        output[outputLen + i].append(arr[n-1])
##    
##    return output
##
##n=int(input())
##li=[int(x) for x in input().split()]
##for j in subset(li):
##    print(*j)














    
