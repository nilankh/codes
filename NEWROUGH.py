#27-aug-2019
'''LIST COMPREHENSION

li=["parikh","ROhan","Ankush"]
li_2d=[[s for s in ele]for ele in li]
for i in range(3):
    for j in range(4):
        x=i*j
        print(x,end=' ')
'''

"""2D LIST ...I/P of the two D list
str=input().split()
n,m=int(str[0]),int(str[1])
li=[[int(j) for j in input().split()]for i in range(n)]
print(li)"""

'''
str=input().split()
n,m=int(str[0]),int(str[1])
li=[[int(j) for j in input().split()]for i in range(n)]
for i in range(n):
    for j in range(m):
        print(li[i][j],end=' ')
    print()'''


#input for jagged list
'''
n=int(input())
li=[[int(j) for j in input().split()] for i in range(n)]
print(li)'''

'''
str=input().split()
n,m=int(str[0]),int(str[1])
b=input().split()
arr=[[int(b[m*i+j])for j in range(m)]for i in range(n)]
'''


'''
str=input().split()
n,m=int(str[0]),int(str[1])
b=str[2:]
arr=[[int(b[m*i+j])for j in range(m)]for i in range(n)]'''
# 3 4 1 2 3 4 5 6 7 8 9 10 11 12
#upar wale ka i/p aiswe hi lenge jaise upar dia hua 3 4 n,m h





'''

l=[int(i) for i in input().strip().split(' ')]
m,n=l[0],l[1]
a=[[l[(j*n)+i+2] for i in range(n)] for j in range(m)]'''

'''smjh aaya 
str=input().split()
n,m=int(str[0]),int(str[1])
li=[[int(j) for j in input().split()]for i in range(n)]
print(li)'''

'''
str=input().split()
n,m=int(str[0]),int(str[1])
b=input().split()
arr=[[int(b[m*i+j])for j in range(m)]for i in range(n)]'''

'''
str=input().split()
n,m=int(str[0]),int(str[1])
b=input().split()#one line
arr=[[int(b[m*i+j])for j in range(m)]for i in range(n)]'''

'''
s=input().split()
m,n=int(s[0]),int(s[1])
li=input().split()
li1=[[int(li[n*x+y])for y in range(n)]for x in range(m)]
for x in range(len(li1)):
    for y in(li1[x]):
        print(y,end=" ")
    print()'''

'''
s=input().split()
n,m=int(s[0]),int(s[1])
b=input().split()
arr=[[int(b[m*i+j])for j in range(m)]for i in range(n)]
for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()'''

'''
n=int(input())
li=[[int(j) for j in input().split()]for i in range(n)]
for row in li:
    for ele in row:
        print(ele,end=' ')
    print()'''

'''
n=int(input())
li=[[int(j) for j in input().split()]for i in range(n)]
for row in li:
    output=' '.join([str(ele)for ele in row])
    print(output)'''
'''
s=input().split()
n,m=int(s[0]),int(s[1])
b=input().split()
arr=[[int(b[m*i+j])for j in range(m)]for i in range(n)]
print(arr[2][3])'''


def sum_multiply(a,b,*more):
    sum_value = a+b
    m_value = a*b
    for i in more:
        sum_value += i
        print(sum_value)
        m_value*=i
        print(m_value)
    return sum_value,m_value
s_m = sum_multiply(2,3,4)
print(s_m)


'''
1 2 3 4 5 
11 12 13 14 15 
21 22 23 24 25 
16 17 18 19 20 
6 7 8 9 10
'''
    
