'''
def spiralPrint(m,n,a):
    k=0
    l=0
    while(k<m and l<n):
        for i in range(l,n):
            print(a[k][i],end=" ")
        k+=1

        for i in range(k,m):
            print(a[i][n-1],end=" ")
        n-=1
        if(k<m):
            for i in range(n-1,(l-1),-1):
                print(a[m-1][i],end=" ")
            m-=1
        if(l<n):
            for i in range(m-1,k-1,-1):
                print(a[i][l],end=" ")
            l+=1
a=input().split()
n,m=int(a[0]),int(a[1])
b=input().split()
arr=[[int(b[m*i+j])for j in range(m)]for i in range(n)]
spiralPrint(n,m,a)'''
def spiralPrint(arr):
    rows=len(arr)
    cols=len(arr[0])
   
    startRow,startCol,endRow,endCol=0,0,rows-1,cols-1
   
    while startRow<=endRow and startCol<=endCol:
        #startRow
        for j in range(startCol,endCol+1):
            print(arr[startRow][j],end=" ")
            #print("jjjj", j)
        startRow+=1
       
        if startRow>endRow or startCol>endCol:
            break
           
        #endCol
        for i in range(startRow,endRow+1):
            print(arr[i][endCol],end=" ")
        endCol-=1
       
        if startRow>endRow or startCol>endCol:
            break
           
        #endRow
        for i in range(endCol,startCol-1,-1):
            print(arr[endRow][i],end=" ")
        endRow-=1
       
        if startRow>endRow or startCol>endCol:
            break
           
        #startCol
        for i in range(endRow,startRow-1,-1):
            #print("loop", i)         
            #print(endRow, startRow)
            print(arr[i][startCol],end=" ")
            #print(arr[i])
        startCol+=1
#Main
r=input().split()
b=r[2:]
arr = [[ int(b[int(r[1])*i+j]) for j in range(int(r[1])) ] for i in range(int(r[0]))]
print(arr)
spiralPrint(arr)





