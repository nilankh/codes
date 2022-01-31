

##def lar_col_sum(li):
##    n=len(li)
##    #print(n)
##    m=len(li[0])
##    #print(m)
##    max_sum=-1
##    max_col_index=-1
##    for j in range(m):
##        sum=0
##        for i in range(n):
##            sum+=li[i][j]
##        if sum>max_sum:
##            max_col_Index=j
##            max_sum=sum
##            print(max_sum)
##    return max_sum,max_col_Index
##
##li=[[1,2,3,4],[8,7,6,5],[9,10,11,12]]
##li = [[1,2,3],[4,5,6]]
##lar_sum,lar_col_Index=lar_col_sum(li)
##print(lar_sum,lar_col_Index)

#another_way
def lar_col_sum(li):
    n=len(li)
    #print(n)
    m=len(li[0])
    #print(m)

    max_sum=-1
    max_col_index=-1
    for j in range(m):
        sum=0
        for ele in li:
            sum+=ele[j]
        if sum>max_sum:
            max_col_Index=j
            max_sum=sum
    return max_sum ,max_col_Index

s = input().split()
n, m = int(s[0]), int(s[1])
b = input().split()
li = [[int(b[m*i+j]) for j in range(m)] for i in range(n)]
lar_sum,lar_col_Index=lar_col_sum(li)
print(lar_sum,lar_col_Index)
##li=[[1,2,3,4],[8,7,6,5],[9,10,11,12]]
##lar_sum,lar_col_Index=lar_col_sum(li)
##print(lar_sum,lar_col_Index)









