def Palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False
s=input()
Palindrome(s)
if(Palindrome(s)):
    print("true")
else:
    print("false")
