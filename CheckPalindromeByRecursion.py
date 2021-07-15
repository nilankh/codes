'''
def CheckPalindrome(s,si,ei):
    if si>ei:
        return True
    if s[si]==s[ei]:
        small=CheckPalindrome(s,si+1,ei-1)
        if small:
            return True
        return False
    return False
s=input()
if(CheckPalindrome(s,0,len(s)-1)):
    print("true")
else:
    print("false")
'''
def palin(s):
    if len(s)<1:
        return True
    elif s[0]==s[-1]:
        return palin(s[1:-1])
    return False
op=palin(input())
if op:
    print("true")
else:
    print("false")
