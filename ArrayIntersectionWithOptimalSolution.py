'''
def merge(a1,a2,a):
    i=0
    j=0
    k=0
    while i<len(a1) and j<len(a2):
        if(a1[i]<a2[j]):
            a[k]=a1[i]
            k=k+1
            i=i+1
        else:
            a[k]=a2[j]
            k=k+1
            j=j+1
    while i<len(a1):
        a[k]=a1[i]
        k=k+1
        i=i+1
    while j<len(a2):
        a[k]=a2[j]
        k=k+1
        j=j+1
def merge_sort(a):
    if len(a)==0 or len(a)==1:
        return
    mid=len(a)//2
    a1=a[0:mid]
    a2=a[mid:]

    merge_sort(a1)
    merge_sort(a2)

    merge(a1,a2,a)

def mergeTwoSortedArrays(arr1,arr2):
    i = 0
    j = 0
    len1 = len(arr1)
    len2 = len(arr2)
    while((i < len1) and (j < len2)):
        if(arr1[i] < arr2[j]):
            i = i + 1
        elif arr2[j]<arr1[i]:
            j = j + 1
        else:
            print(arr1[i])
            i=i+1
            j=j+1
def intersection(arr1, arr2):
    merge_sort(arr1)
    merge_sort(arr2)
    
    mergeTwoSortedArrays(arr1,arr2)

n1=int(input())
arr1=list(int(i) for i in input().strip().split(' '))
n2=int(input())
arr2=list(int(i) for i in input().strip().split(' '))
intersection(arr1, arr2)'''
#2nd method bonary wala
def merge(a1,a2,a):
    i=0
    j=0
    k=0
    while i<len(a1) and j<len(a2):
        if(a1[i]<a2[j]):
            a[k]=a1[i]
            k=k+1
            i=i+1
        else:
            a[k]=a2[j]
            k=k+1
            j=j+1
    while i<len(a1):
        a[k]=a1[i]
        k=k+1
        i=i+1
    while j<len(a2):
        a[k]=a2[j]
        k=k+1
        j=j+1
def merge_sort(a):
    if len(a)==0 or len(a)==1:
        return
    mid=len(a)//2
    a1=a[0:mid]
    a2=a[mid:]

    merge_sort(a1)
    merge_sort(a2)

    merge(a1,a2,a)
def BinarySearch(a,x,si,ei):
    if si>ei:
        return -1
    mid=(si+ei)//2
    if a[mid]==x:
        return mid
    elif a[mid]>x:
        return BinarySearch(a,x,si,mid-1)
    else:
        return BinarySearch(a,x,mid+1,ei)
def intersection(arr1, arr2):
    # Please add your code here
    a = len(arr1)
    b = len(arr2)
    merge_sort(arr1)
    merge_sort(arr2)
    i , j = 0, 0
    while i < a and j < b:
        if arr1[i] > arr2[j]:
            j = j + 1
        elif arr1[i] < arr2[j]:
            i = i + 1
        else:
            print(arr1[i])
            i = i + 1
            j = j + 1

#17-09-19 00:29

#Shubham Shrivastava


n1=int(input())
arr1=list(int(i) for i in input().strip().split(' '))
n2=int(input())
arr2=list(int(i) for i in input().strip().split(' '))
intersection(arr1, arr2)













