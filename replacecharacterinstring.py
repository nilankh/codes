
def replace(str,char1,char2):
    newStr=""
    for char in str:
        if(char == char1):
            newStr+=char2
        else:
            newStr+=char
    return newStr
str="fajssjssjsklhs"
str=replace(str,'s','d')
print(str)
'''
def replace(str,char1,char2):
    newStr=""
    for char in str:
        if(char==char1):
            newStr+=char2
        else:
            newStr+=char
    return newStr


str=input("ENTER A STRING:")
ch=input("which char you want to replace:")
new=input("enter new char")
str=replace(str,ch,new)
print(str)'''
