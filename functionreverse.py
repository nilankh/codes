'''def reverse_l(li):
    length=len(li)
    for i in range(length//2):
        li[i],li[length-i-1]=li[length-i-1],li[i]
n=int(input("enter size:"))
li=[int(x) for x in input().split(',')]
reverse_l(li)
print(li)
'''

'''2nd way
def reverse_l(li):
    length=len(li)
    for i in range(length//2):
        li[i],li[-i-1]=li[-i-1],li[i]
n=int(input("enter size:"))
li=[int(x) for x in input().split(',')]
reverse_l(li)
print(li)'''

'''3rd way with help of slicing operator'''
def reverse_l(li):
    li=li[::-1]
    print(li)
n=int(input("enter size:"))
li=[int(x) for x in input().split(',')]
reverse_l(li)
#print(li)
