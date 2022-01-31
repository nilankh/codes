'''


li_1=[1,2,3,4,5]
li_2=[2,4,6,7]
li_intersection=[]
for ele in li_1:
    for ele_2 in li_2:
        if ele==ele_2:
            li_intersection.append(ele)
print(li_intersection)'''

li_1=[1,2,3,4,5]
li_2=[2,4,6,7]
li_inter=[ele for ele in li_1 for ele_2 in li_2 if ele==ele_2]
print(li_inter)


'''LIST COMPREHENSION EXAMPLES


li=["parikh","rohan","ankush"]
li_d=[[s for s in ele] for ele in li]
print(li_d)'''

'''
li=[1,2,3,4]
li_new=[]
for ele in li:
    li_new.append(ele**2)
print(li_new)'''
'''
li=[1,2,3,4]
li_new=[ele**2 for ele in li]
print(li_new)'''
'''
li=[1,2,3,4]
li_even=[ele**2 for ele in li if ele%2==0]
print(li_even)'''

'''
li=[1,2,3,4,5,6,7,8,9]
li_new=[]
for ele in li:
    if ele % 2 == 0:
        if ele % 3 == 0:
            li_new.append(ele)
print(li_new)'''
'''
li=[1,2,3,4,5,6,7,8,9]
li_new=[ele for ele in li if ele % 2 == 0 if ele % 3 == 0]
print(li_new)'''

''''
li=[1,2,3,4,5]
li_new=[ele**2 if ele%2==0 else ele for ele in li]
print(li_new)'''

'''
s="PARIKH"
li=[s for ele in s]
print(li)'''

'''
s="PARIKH"
li=[ele for ele in s]
print(li)'''

'''
li=["Parikh","rohan","ankush"]
li_2d=[[s for s in ele]for ele in li]
print(li_2d)'''





##for jagged2d list
##n = int(input())
##li = [[int(k) for k in input().split()]for i in range(n)]
##for row in li:
##    for ele in row:
##        print(ele, end =' ')
##    print()

str = input().split()
n, m = int(str[0]), int(str[1])
b = input().split()
arr = [[ int(b[m*i+j])for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        print(arr[i][j], end =' ')
    print()



    





