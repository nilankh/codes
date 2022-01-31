def checkPalindrome(str):
    i = 0
    j = len(str) - 1
    while(i < j):
        if str[i] != str[j]:
            return False
        i += 1
        j -= 1
    return True
    
str = input()
ans = checkPalindrome(str)
if ans:
    print("true")
else:
    print("false")
