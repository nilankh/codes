##Arrange Numbers In Array
##Send Feedback
##Given a number n, put all elements from 1 to n in an array in order - 1,3,.......4,2.
##Input Format :
## Integer n
##Output Format :
## Elements of the array separated by space.
##Constraints :
##1 <= n <= 10^7
##Sample Input 1 :
##6
##Sample Output 1 :
## 1 3 5 6 4 2
##Sample Input 2 :
##9
##Sample Output 2 :
## 1 3 5 7 9 8 6 4 2

def arrange(n):
    arr = [0] * n
    left = 0
    right = n - 1
    number = 1
    while(left < right):
        arr[left] = number
        left += 1
        number += 1
        arr[right] = number
        right -= 1
        number += 1
    if(left == right):
        arr[left] = number
    return arr

n = int(input())
arr = arrange(n)
for number in arr:
    print(number, end = " ")
print()
