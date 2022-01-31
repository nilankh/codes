'''
def checkArmstrong(num):
# initialize sum
    sum = 0
# find the sum of the cube of each digit
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
# display the result
    if num == sum:
       return True
    else:
       return False
num=int(input())
if(checkArmstrong(num)):
    print("true")
else:
    print("false")

def printfreq(s,k):
    words=s.split()
    d={}
    for w in words:
        d[w]=d.get(w,0)+1
    for w in d:
        if d[w]==k:
            print(w)
s = input()
k = int(input())
printfreq(s,k)'''

def reverse(arr):
    for i in range(len(arr)//2):
        arr[i],arr[len(arr)-i-1]=arr[len(arr)-i-1],arr[i]
        print(arr)
arr = [5,4,3,2,1]
reverse(arr)








    
