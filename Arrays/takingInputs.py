#line seperated input
'''
n = int(input())
print(n)
li = []
for i in range(n):
    curr = int(input())
    li.append(curr)
'''

#space seperated inpput

n = int(input())
str = input()
li = []
str_split = str.split(' ')
#print(str_split)
for ele in str_split:
    li.append(int(ele))
print(li)

li = [int(x) for x in input().split()]
print(li)
