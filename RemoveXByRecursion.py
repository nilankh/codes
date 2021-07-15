def RemoveX(s):
    if len(s)==0:
        return s
    if s[0]=='x':
        return RemoveX(s[1:])
    return s[0]+RemoveX(s[1:])
s=input()
print(RemoveX(s))
