#revise pattern problems 11-aug-19
'''     *******
        *******
        *******
        *******
        *******
        *******
        *******

n=int(input())
i=1
while i<=n:
    j=1
    while j<=n:
        print('*',end='')
        j=j+1
    print()
    i=i+1'''


'''
111111
222222
333333
444444
555555
666666


n=int(input())
i=1
while i<=n:
    j=1
    while j<=n:
        print(i,end='')
        j=j+1
    print()
    i=i+1'''

'''
123456
123456
123456
123456
123456
123456

n=int(input())
i=1
while i<=n:
    j=1
    while j<=n:
        print(j,end='')
        j=j+1
    print()
    i=i+1'''
   
'''
654321
654321
654321
654321
654321
654321

n=int(input())
i=1
while i<=n:
    j=1
    while j<=n:
        print(n-j+1,end='')
        j=j+1
    print()
    i=i+1'''

'''
1
12
123
1234
12345
123456

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
1 
2 3 
3 4 5 
4 5 6 7 
5 6 7 8 9 
6 7 8 9 10 11 

n=int(input())
i=1
while i<=n:
    j=1
    p=i
    while j<=i:
        print(p,end=' ')
        p=p+1
        j=j+1
    print()
    i=i+1'''
'''
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 21 
22 23 24 25 26 27 28 

n=int(input())
i=1
p=1
while i<=n:
    j=1
    while j<=i:
       print(p,end=' ')
       p=p+1
       j=j+1
    print()
    i=i+1'''
'''
1 
1 1 
1 1 1 
1 1 1 1 
1 1 1 1 1
n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print(1,end=' ')
        j=j+1
    print()
    i=i+1'''
        
'''
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

n=int(input())
i=1
while i<=n:
    j=1
    while j<=n-i+1:
        print('*',end=' ')
        j=j+1
    print()
    i=i+1'''

'''
     *
    **
   ***
  ****
 *****
******

n=int(input())
i=1
while i<=n:
    spaces=1
    while spaces<=n-i:
        print(' ',end='')
        spaces=spaces+1
    star=1
    while star<=i:
        print('*',end='')
        star=star+1
    print()
    i=i+1'''
'''
    1
   121
  12321
 1234321
123454321


n=int(input())
i=1
while i<=n:
    #spaces sequences
    spaces=1
    while spaces<=n-i:
        print(' ',end=' ')
        spaces=spaces+1
    #increasing sequences
    p=1
    j=1
    while j<=i:
        print(p,end=' ')
        p=p+1
        j=j+1
    #decreasing sequences
    p=i-1
    while p>=1:
        print(p,end=' ')
        p=p-1
    print()
    i=i+1'''
'''
1
11
121
1221
n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        if(j==1 or j==i):
            print(1,end='')
        else:
            print(2,end='')
        j=j+1
    print()
    i=i+1'''
'''
1        1
12      21
123    321
1234  4321
1234554321

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
        
    print()
    i=i+1'''

''' 12345
    23456
    34567
    45678
    56789
n=int(input())
i=1
while i<=n:
    j=1
    p=i
    while j<=n:
        print(p,end='')
        p=p+1
        j=j+1
    i=i+1'''

''' 
1234
5678
9101112
13141516

n=int(input())
i=1
p=1
while i<=n:
    j=1
    while j<=n:
        print(p,end='')
        p=p+1
        j=j+1
    print()
    i=i+1''' 

'''
1
11
202
3003
40004

n=int(input())
print(1)
i=1
while i<=n:
    j=0
    while j<=i:
        if(j==0 or j==i):
            print(i,end='')
        else:
            print(0,end='')
        j=j+1
    print()
    i=i+1'''
    
'''start from patter17.py'''

'''
*0000*0000*
0*000*000*0
00*00*00*00
000*0*0*000
0000***0000


n=int(input())
i=0
k=2*n
while i<n:
    j=0
    while j<2*n+1:
        if(j==n):
            print('*',end='')
        elif(j==i):
            print('*',end='')
        elif(j==k):
            print('*',end='')
        else:
            print(0,end='')
        j=j+1
    k=k-1
    print()
    i=i+1'''
    
'''
    1
   12
  123
 1234
12345

n=int(input())
i=1
while i<=n:
    spaces=1
    while spaces<=n-i:
        print(' ',end='')
        spaces=spaces+1
    j=1
    while j<=i:
        print(j,end='')
        j=j+1
    print()
    i=i+1'''

'''
   1
  23
 456
78910

n=int(input())
i=1
p=1
while i<=n:
    spaces=1
    while spaces<=n-i:
        print(' ',end='')
        spaces=spaces+1
    j=1
    while j<=i:
        print(p,end='')
        p=p+1
        j=j+1
    print()
    i=i+1'''

'''
11111
0000
111
00
1

n=int(input())
i=1
while i<=n:
    j=1
    while j<=n-i+1:
        if i%2==0:
            print(0,end='')
        else:
            print(1,end='')
        j=j+1
    print()
    i=i+1'''
'''
1
22
303
4004
50005
n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        if(j==i or j==1):
            print(i,end='')
        else:
            print(0,end='')
        j=j+1
    print()
    i=i+1'''
'''
ABCDE
ABCDE
ABCDE
ABCDE
ABCDE
n=int(input())
i=1
while i<=n:
    j=1
    while j<=n:
        charP=chr(ord('A')+j-1)
        print(charP,end='')
        j=j+1
    print()
    i=i+1'''

'''
ABCDEF
BCDEFG
CDEFGH
DEFGHI
EFGHIJ
FGHIJK
n=int(input())
i=1
while i<=n:
    j=1
    start_char=chr(ord('A')+i-1)
    while j<=n:
        charP=chr(ord(start_char)+j-1)
        print(charP,end='')
        j=j+1
    print()
    i=i+1'''
'''
A
BB
CCC
DDDD

n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        charP=chr(ord('A')+i-1)
        print(charP,end='')
        j=j+1
    print()
    i=i+1'''
'''
ABCD
EFGH
IJKL
MNOP
n=int(input())
i=1
p=ord('A')
while i<=n:
    j=1
    while j<=n:
        c=chr(p)
        print(c,end='')
        p=p+1
        j=j+1
    print()
    i=i+1'''

'''
    1
   212
  32123
 4321234
543212345

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
        
    
*
 * *
   * * *
     * * * *
   * * *
 * *
*

n always be odd

'''
'''
* 
 * * 
  * * * 
   * * * * 
  * * * 
 * * 
* 

n=int(input())
increasing=(n+1)//2
decreasing=n-increasing
i=1
while i<=increasing:
    spaces=1
    while spaces<=i-1:
        print(' ',end='')
        spaces=spaces+1
    j=1
    while j<=i:
        print('* ',end='')
        j=j+1
    print()
    i=i+1
#2nd half ke lia
i=1
while i<=decreasing:
    #2nd half ka spaces bole toa printing spaces 1st row has 2 spaces 2nd row has 1 spaces,so ith will have decreasing-i spaces
    spaces=1
    while spaces<=decreasing-i:
        print(' ',end='')
        spaces=spaces+1
    #printing stars 1st row has 3 star 2nd row has 2,so ith will have decreasing-i+1 stars
    j=1
    while j<=decreasing-i+1:
        print('* ',end='')
        j=j+1
    print()
    i=i+1'''
 


'''SelectionSort
def selectionSort(arr):
    length=len(arr)
    for i in range(length-1):
        minIndex=i
        for j in range(i+1,length):
            if(arr[j]<arr[minIndex]):
                minIndex=j
        arr[i],arr[minIndex]=arr[minIndex],arr[i]

arr=[12,97,63,45,9,8,1]
selectionSort(arr)
print(*arr)
n=int(input())
arr=[int(x)for x in input().split()]
selectionSort(arr)
print(*arr)'''

'''bubble Sort
def bubbleSort(arr):
    length=len(arr)
    for i in range(length-1):
        for j in range(length-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]

n=int(input())
arr=[int(x) for x in input().split()]
bubbleSort(arr)
print(*arr)'''

''' insertion Sort

def insertionSort(arr):
    length=len(arr)
    for i in range(1,length):
        j=i-1
        temp=arr[i]
        while(j>=0 and arr[j]>temp):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=temp
n=int(input())
arr=[int(x) for x in input().split()]
insertionSort(arr)
print(*arr)'''


'''binarySearch
def binarySearch(arr,element):
    start=0
    end=len(arr)-1
    while start<=end:
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

'''LinearSearch
def linearSearch(li,ele):
    for i in range(len(li)):
        if li[i]==ele:
            return i
    return -1
n=int(input())
li=[int(x) for x in input().split()]
ele=int(input())
index=linearSearch(li,ele)
print(index)'''

'''merge two sorted array
def mergeSortedArrays(arr1,arr2):
    i=0
    j=0
    len1=len(arr1)
    len2=len(arr2)

    arr=[]

    while((i<len1) and (j<len2)):
        if(arr1[i]<arr2[j]):
            arr.append(arr1[i])
            i=i+1
        else:
            arr.append(arr2[j])
            j=j+1
    while(i<len1):
        arr.append(arr1[i])
        i=i+1
    while(j<len2):
        arr.append(arr2[j])
        j=j+1
    return arr
arr1=[1,4,9,10]
arr2=[2,3,6,7,8]
arr=mergeSortedArrays(arr1,arr2)
print(arr)'''

'''pushZerosToEnd
def pushZerosToEnd(arr):
    length=len(arr)
    j=0
    for i in range(0,length):
        if(arr[i]==0):
            continue
        arr[j]=arr[i]
        j=j+1
    while(j<n):
        arr[j]=0
        j=j+1
n=int(input())
arr=[int(x) for x in input().split()]
pushZerosToEnd(arr)
print(*arr)'''

'''Rotate Array
def Reverse(arr,start,end):
    while(start<end):
        arr[start],arr[end]=arr[end],arr[start]
        start=start+1
        end=end-1
def Rotate(arr,d):
    length=len(arr)

    Reverse(arr,0,length-1)
    Reverse(arr,0,length-d-1)
    Reverse(arr,length-d,length-1)

n=int(input())
arr=[int(x) for x in input().split()]
d=int(input())
Rotate(arr,d)
print(*arr)'''

''''CHECK ARRAY ROTATION
def checkArrayRotation(arr):
    minval=min(arr)
    count=0
    for i in arr:
        if i==minval:
            break
        else:
            count+=1
    print(count)
n=int(input())
arr=[int(x) for x in input().split()]
checkArrayRotation(arr)'''


'''Find Unique
def findUnique(arr):
    length=len(arr)
    for i in range(0,length):
        for j in range(0,length):
            if(arr[i]==arr[j] and i!=j):
                break
        else:
            return arr[i]

n=int(input())
arr=[int(x) for x in input().split()]
number=findUnique(arr)
print(number)'''
'''
def findUnique(arr):
    length=len(arr)
    for i in range(0,length):
        for j in range(0,length):
            if(arr[i]==arr[j] and i!=j):
                break
        else:
            print( arr[i])

n=int(input())
arr=[int(x) for x in input().split()]
findUnique(arr)
#print(number)'''
''' find duplicates
def findDuplicates(arr):
    length=len(arr)
    for i in range(0,length):
        for j in range(i+1,length):
            if(arr[i]==arr[j]):
                print(arr[i])
n=int(input())
arr=[int(x) for x in input().split()]
findDuplicates(arr)'''

'''intersection
n1=int(input())
li_1=[int(x) for x in input().split()]
n2=int(input())
li_2=[int(x) for x in input().split()]
li_inter=[ele for ele in li_1 for ele_2 in li_2 if ele==ele_2]
print(*li_inter)'''

''' Pairsum
def pairSum(arr):
    for i in range(0,n):
        for j in range(i+1,n):
            if(arr[i]+arr[j]==sum):
                if(arr[i]<arr[j]):
                    print(arr[i]," ",arr[j],sep="")
                else:
                    print(arr[j]," ",arr[i],sep="")
n=int(input())
arr=[int(x) for x in input().split()]
sum=int(input())
pairSum(arr)'''

'''Triplet Sum
def TripletSum(arr):
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if(arr[i]+arr[j]+arr[k]==sum):
                    print(arr[i],arr[j],arr[k])

n=int(input())
arr=[int(x) for x in input().split()]
sum=int(input())
TripletSum(arr)'''

'''sort01
def sort01(arr):
    length=len(arr)
    start=0
    end=length-1
    while(start<end):
        while(arr[start]==0 and start<end):
            start=start+1
        while(arr[end]==1 and start<end):
            end=end-1
        if(start<end):
            temp=arr[start]
            arr[start]=arr[end]
            arr[end]=temp
            start=start+1
            end=end-1
n=int(input())
arr=[int(x) for x in input().split()]
sort01(arr)
print(arr)'''


''' sort01 with count
def sort01(arr):
    length=len(arr)
    count=0
    for i in range(length):
        if(arr[i]==0):
            count+=1
    for i in range(count):
        print(0,end=' ')
    for i in range(length-count):
        print(1,end=' ')
n=int(input())
arr=[int(x) for x in input().split()]
sort01(arr)'''
'''
n=int(input())
arr=[int(x) for x in input().split()]
arr.sort()
print(arr)'''

'''SECOND LARGEST
def findSecondLargest(arr):
    largest=-2147483648
    secondLargest=-2147483648
    for num in arr:
        if(num>secondLargest):
            if(num>largest):
                secondLargest=largest
                largest=num
            elif(num!=largest):
                secondLargest=num
    return secondLargest
n=int(input())
arr=[int(x) for x in input().split()]
num=findSecondLargest(arr)
print(num)'''
'''sort012
def sort012(arr):
    length=len(arr)

    count0=0
    count1=0
    count2=0
    for i in range(length):
        if(arr[i]==0):
            count0+=1
        if(arr[i]==1):
            count1+=1
        if(arr[i]==2):
            count2+=1
    for i in range(count0):
        print(0,end=" ")
    for i in range(count1):
        print(1,end=" ")
    for i in range(count2):
        print(2,end=" ")

n=int(input())
arr=[int(x) for x in input().split()]
sort012(arr)'''
'''
def Rotate(arr,d):
    length=len(arr)
    for i in range(d):         
        temp = arr[0] 

        for i in range(length-1): 
            arr[i] = arr[i + 1] 
        arr[length-1] = temp 

n=int(input())
arr=[int(x) for x in input().split()]
d=int(input())
Rotate(arr,d)    
print(*arr)
'''

'''SUM OF ARRAYS
def arr_sum(arr1,arr2):
    i=len(arr1)-1
    j=len(arr2)-1
    l=[]
    carry=0

    while i>=0 and j>=0:
        sum=arr1[i]+arr2[j]+carry
        carry=sum//10
        l.append(sum%10)
        i-=1
        j-=1
    while i>=0:
        sum=arr1[i]+carry
        carry=sum//10
        l.append(sum%10)
        i-=1
    while j>=0:
        su=arr2[j]+carry
        carry=sum//10
        l.append(sum%10)
        j-=1
    l.append(carry)
    l.reverse()

    return l


n1=int(input())
arr1=[int(x) for x in input().split()]
n2=int(input())
arr2=[int(x) for x in input().split()]
l=arr_sum(arr1,arr2)
print(*l)
'''

'''
def replace(str,char1,char2):
    newStr=""
    for char in str:
        if(char==char1):
            newStr+=char2
        else:
            newStr+=char
    return newStr


str=input("ENTER A STRING:")
ch=input("which char you want to replace:")
new=input("enter new char")
str=replace(str,ch,new)
print(str)'''

'''
def countInString(str):
    v,c,d,s=0,0,0,0
    for char in str:
        if((char>='a' and char<='z') or (char>='A' and char<='Z')):
            char=char.lower()
            if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
                v+=1
            else:
                c+=1
        elif(char>='0' and char<='9'):
            d+=1
        else:
            s+=1
    return v,c,d,s
str="NiLaNk NiKhIl 123 @!aaa"
v,c,d,s = countInString(str)
print(v,c,d,s)'''

'''BInary to decimal
def binTodecimal(binary):
    i=0
    s=0
    while(binary):
        s=s+pow(2,i)*(binary%10)
        binary=binary//10
        i=i+1
    return(s)
binary=int(input())

s=binTodecimal(binary)
print(s)'''

'''
def decimalToBinary(decimal):
    i=0
    while(decimal):
        s[decimal]=decimal%10
        decimal=decimal//2
        i=i+1

decimal=int(input("ENTER A DECIMAL NO:"))
decimalToBinary(decimal)
print()
''''




