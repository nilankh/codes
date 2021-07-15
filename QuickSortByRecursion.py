def partition(a,si,ei):
    #3steps
    #1> FInd pivot
    #2 Place pivot at its position
    #3 Ensure towards left <= x towards right > x
    #4 finally pivot position return krega
    
    pivot=a[si]
    #Find number of elements smaller than pivot
    c=0
    for i in range(si,ei+1):
        if a[i]<pivot:
            c=c+1
            #print('count ka value',c)
    a[si+c],a[si]=a[si],a[si+c]
    #print(a)
    pivot_index=si+c
    i=si
    j=ei
    while i<j:
        if a[i]<pivot:
            i=i+1
        elif a[j]>=pivot:
            j=j-1
        else:
            a[i],a[j]=a[j],a[i]
            #print("else wla ",a)
            i=i+1
            j=j-1
    #print(pivot_index)
    return pivot_index
            
def quick_sort(a,si,ei):
    if si >= ei:
        return
    pivot_index=partition(a,si,ei)
    quick_sort(a,si,pivot_index-1)
    quick_sort(a,pivot_index+1,ei)

n=int(input())
a=[int(m)for m in input().split()]
quick_sort(a,0,len(a)-1)
print(a)





