'''
s=input()
i=1
while(i<len(s)):
    if(s[i]==s[i-1]):
        j=i+1
        s=s[:i]+s[j:]
    else:
        i+=1
print(s)'''


def removeDuplicates(s):
    index=1
    while index<len(s):
        if s[index]==s[index-1]:
            nextIndex=index+1
            '''length=len(s)
            while nextIndex<length and s[nextIndex]==s[index]:
                nextIndex+=1'''
            s=s[:index]+s[nextIndex:]
        else:
            index+=1
    return s
s=input()
print(removeDuplicates(s))
