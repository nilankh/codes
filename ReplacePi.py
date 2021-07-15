def ReplacePi(s):
    if len(s)==0 or len(s)==1:
        return s
    if s[0]=='p' and s[1]=='i':
        smallOutput=ReplacePi(s[2:])
        return '3.14'+smallOutput
    else:
        smallOutput=ReplacePi(s[1:])
        return s[0]+smallOutput
s=input()
print(ReplacePi(s))
