'''
n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end='')
        j=j+1
    print()
    i=i+1'''


'''
n=int(input())
i=1
while i<=n:
    #spaces sequence
    spaces=1
    while spaces<=n-i:
        print(' ',end='')
        spaces=spaces+1
    j=i
    while j>0:
        print(j,end='')
        j=j-1
    i=i+1
    print()'''

'''
n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end='')
        j=j+1
    spaces=1    
    while spaces<=2*n-2*i:
        print(' ',end='')
        spaces=spaces+1
    j=i
    while j>0:
        print(j,end='')
        j=j-1
    i=i+1
    print()'''


'''
n=int(input())
i=1
while i<=n:
    spaces=1
    while spaces<=n-i:
        print(' ',end='')
        spaces=spaces+1
    
    j=i
    while j>0:
        print(j,end='')
        j=j-1
   
  
    j=2
    while j<=i:
        print(j,end='')
        
        j=j+1
   
    print()
    i=i+1'''

'''
n=int(input())
n1=(n//2+1)
i=1
while i<=n1:
    spaces=1
    while spaces<=n1-i:
        print(' ',end='')
        spaces=spaces+1
    j=1
    while j<=2*i-1:
        print('*',end='')
        j=j+1
    print()
    i=i+1
n2=n-n1
i=n2
while i>=1:
    spaces=1
    while spaces<=n1-i:
        print(' ',end='')
        spaces=spaces+1
    j=1
    while j<=2*i-1:
        print('*',end='')
        j=j+1
    print()
    i=i-1
'''


'''
def checkPalindrome(num):
#Implement Your Code Here
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=s*10+dig
        num=num//10
    if(temp==rev):
        print('true')
    else:
        print('false')
'''

'''
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
'''




'''
def checkPalindrome(num):
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        return True
    else:
        return False
num=int(input())
if(checkPalindrome(num)):
    print("true")
else:
    print("false")
'''



'''
swap_alternate(arr):
    n = len(arr)
    for i in range(0,n,2):
        if i+1 < n:
            arr[i], arr[i+1] = arr[i+1], arr[i]

n = int(input())
arr = [int(i) for i in input().split()]
swap_alternate(arr)
for ele in arr:
    print(ele, end = ' ')'''


'''def findSingle( ar, n): 
      
    res = ar[0] 
    for i in range(1,n): 
        res = res ^ ar[i] 
      
    return res 
n=int(input()) 
ar = [int(i) for i in input().split()]
print ("Element occuring once is", findSingle(ar, len(ar))) '''

'''
def printRepeating(arr, size): 
  
    print(end = '') 
    for i in range (0, size): 
        for j in range (i + 1, size): 
            if arr[i] == arr[j]: 
                print(arr[i], end = ' ') 
      
n=int(input())
arr = [int(i) for i in input().split()]
arr_size = len(arr) 
printRepeating(arr, arr_size) '''


'''
def printPairs(arr, n, sum): 
  
    # count = 0  
  
    # Consider all possible  
    # pairs and check their sums 
    for i in range(0, n ): 
        for j in range(i + 1, n ): 
            if (arr[i] + arr[j] == sum): 
                print("(", arr[i],  
                      ", ", arr[j],  
                      ")", sep = "") 
  
  
# Driver Code 
arr = [1, 5, 7, -1, 5] 
n = len(arr) 
sum = 6
printPairs(arr, n, sum) '''

'''
def binarySearch(arr,element):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=(start+end)//2
        if(arr[mid]==element):
           return mid
        elif(arr[mid]<element):
           start=mid+1
        else:
           end=mid-1
    return -1
n=int(input())
arr=[int(x) for x in input().split()]
element=int(input())
index=binarySearch(arr,element)
print(index)'''

'''def selectionSort(arr):
    length=len(arr)
    for i in range(length-1):
        minIndex=i
        for j in range(i+1,length):
            if(arr[j]<arr[minIndex]):
                minIndex=j
        arr[i],arr[minIndex]=arr[minIndex],arr[i]
n=int(input())
arr=[int(x) for x in input().split()]
selectionSort(arr)
print(arr)'''


'''
## Print output as specified in the question.
def bubbleSort(arr):
    length=len(arr)
    #i is for n-1 rounds
    for i in range(length-1):
        #j is for in each iteration you need to go till length-1-i position
        for j in range(length-1-i):#doubt
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
n=int(input())
arr=[int(x) for x in input().split()]
bubbleSort(arr)
print(arr)'''

'''
def fact(a):
    a_fact=1
    for r in range(1,a+1):
        a_fact=a_fact*r
    return a_fact

n=int(input())
r=int(input())
n_fact=fact(n)
r_fact=fact(r)
n_r_fact=fact(n-r)
ans=n_fact//(r_fact*n_r_fact)
print(ans)'''

'''def sum(a,b):
    c=a+b
    return c
a=int(input())
b=int(input())
c=sum(a,b)
print(c)'''

'''
def fact(n):
    n_fact=1
    for i in range(1,n+1):
        n_fact=n_fact*i
    return(n_fact)
def ncr(n,r):
    n_fact=fact(n)
    r_fact=fact(r)
    n_r_fact=fact(n-r)
    ans=n_fact//(r_fact*n_r_fact)
    return ans
n=int(input())
r=int(input())
ans=ncr(n,r)
print(ans)'''

'''
def fibo(n):
    i=0
    a=0
    b=1
    while(i<n):
        if(i<=1):
            c=i
        else:
            c=a+b
            a=b
            b=c
        i=i+1
        print(c,end=',')
n=int(input())
fibo(n)'''

'''
n = int(input('Enter the number : '))
sum = 0
temp = n
while (n):
    i = 1
    fact = 1
    rem = int(n % 10)

    while(i <= rem):
        fact = fact * i
        i = i + 1
    sum = sum + fact
    n = int(n / 10)

if(sum == temp):
    print(temp,end = '')
    print(' is a strong number')
else:
    print(temp,end = '') 
    print(' is not a strong number')'''
    
'''
sum1=0
num=int(input("Enter a number:"))
temp=num
while(num):
    i=1
    f=1
    r=num%10
    while(i<=r):
        f=f*i
        i=i+1
    sum1=sum1+f
    num=num//10
if(sum1==temp):
    print("The number is a strong number")
else:
    print("The number is not a strong number")'''

'''
def checkArmstrong(num):
    temp=num
    length=len(str(num))
    sum=0
    while(num>0):
        rem=num%10
        sum=sum+rem**length
        num=num//10
    if(temp==sum):
        return True
    else:
        return False

num=int(input())
isArmstrong=checkArmstrong(num)
if(isArmstrong):
    print("true")
else:
    print("false")'''

'''
import math
start = int(input('Enter start value : '))
end = int(input('Enter end value : '))
result = 0
n = 0
for i in range(start+1 ,end,1):
    temp2 = i
    temp1 = i
   
    while (temp1 != 0):
        temp1 = temp1//10
        n = n + 1

    while (temp2 != 0):
        remainder = temp2 % 10
        result = result + remainder**n
        temp2 = temp2//10

    if (result == i):
        print(i,' ')

    n = 0
    result = 0'''

##str = input()
##rev = ""
##num1 = len(str);
##j = num1 - 1
##for i in range(0, num1):
##   rev = rev + str[j]
##   j = j - 1
##print(rev)

def printPathHelper(x, y, maze, n, solution):
   #destination Cell
   if x == n - 1 and y == n - 1:
      solution[x][y] = 1
      print(solution)
      return

   if x < 0 or y < 0 or x >=n or y >=n or maze[x][y] == 0 or solution[x][y] == 1:
      return

   solution[x][y] = 1

   #down
   printPathHelper(x + 1, y, maze, n, solution)

   #right
   printPathHelper(x, y + 1, maze, n, solution)

   #top
   printPathHelper(x - 1, y, maze, n, solution)

   #left
   printPathHelper(x, y - 1, maze, n, solution)

   solution[x][y] = 0
   return


def printPath(maze):
   n = len(maze)
   solution = [[0 for j in range(n)]for i in range(n)]
   printPathHelper(0, 0, maze, n, solution)
n = int(input())
maze = []
for i in range(n):
   row = [int(ele) for ele in input().split()]
   maze.append(row)
printPath(maze)









        
    




















