'''
def checkRedundant(string):
    s=[]
    for char in string:
        if char!=')':
            s.append(char)
        else:
            p=s.pop()
            flag=True
            while(p!='('):
                if p=='+' or p=='/' or p=='*' or p=='-':
                    flag=False
                p=s.pop()
            if flag==True:
                return True
    return False    
string=input()
if checkRedundant(string):
    print("true")
else:
    print("false")'''
def checkRedundant(string):
    
    count = 0
    s = []
    for i in string:
        if i != ')':
    
            s.append(i)
            
    
        if (i == ')') :
            while s[-1] != '(':
                s.pop()
                count += 1
            s.pop()
            if count == 0 or count == 1:
                return True
            
        count = 0
    return False
    

string = input()
ans = checkRedundant(string)
if ans is True:
    print('true')
else:
    print('false')















                   
            
