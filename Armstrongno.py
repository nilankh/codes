def checkArmstrong(num):
    orig=num
    length=len(str(num))
    sum = 0
    while (num>0):
        rem=num%10
        sum = sum+rem**length
        num = num//10
    if orig==sum:
        return True
    else:
        return False

num = int(input())
isArmstrong = checkArmstrong(num)
if(isArmstrong):
    print('true')
else:
    print('false')
