
def StringToInteger(str):
    if len(str)==0:
        return 0
    if len(str)==1:
        return int(str[0])
    else:
        return int(str[-1])+10*StringToInteger(str[:-1])
    

str=input()
z=StringToInteger(str)

print(z)
'''

def stI(n):
    if len(n)==1:
        return ord(n[0])-48
    return (10 **len(n[1:]) * (ord(n[0])-48)) + stI(n[1:])
n=input()
print(stI(n))
'''
