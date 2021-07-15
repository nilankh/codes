def ReplaceChar(str,ch,new):
    if len(str)==0:
        return str
    smallOutput=ReplaceChar(str[1:],ch,new)
    if str[0]==ch:
        return new+smallOutput
    else:
        return str[0]+smallOutput
    
str=input()
replace = input().strip().split()
ch=replace[0]
new=replace[1]
str=ReplaceChar(str,ch,new)
print(str)
