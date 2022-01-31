def FindSecondLargest(arr):
    largest=-2147483648
    secondLargest=-2147483648
    for number in arr:
        if(number>secondLargest):
            if(number>largest):
                secondLargest=largest
                largest=number
            elif(number!=largest):
                secondLargest=number
    return secondLargest

n=int(input())
arr=[int(x) for x in input().split()]
number=FindSecondLargest(arr)
print(number)
