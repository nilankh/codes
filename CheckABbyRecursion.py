def CheckAB(str):
    if(len(str)==0):
        return True
    if(str[0]=='a'):
        if(len(str[1:])>1 and str[1:3]=='bb'):
            return CheckAB(str[3:])
        else:
            return CheckAB(str[1:])
    else:
        return False
str=input()
if(CheckAB(str)):
    print("true")
else:
    print("false")
'''
def CheckAB(n):
    if(n[0]!="a"):
        return False
    if(len(n)<3):
        if(n[1]=="a"):
            return True
        else:
            return False
    i=0
    while(i<len(n)-2):
        if(n[i]=="b" and n[i+1]=="b" and n[i+2]=="a"):
            i+=2
        elif(n[i]=="b" and n[i+1]!="b"):
            return False
        elif(n[i]=="b" and n[i+1]=="b" and n[i+2]!="a"):
            return False
        i+=1
    return True    

n=input()
z=CheckAB(n)
if z :
    print("true")
else:
    print("false")'''
