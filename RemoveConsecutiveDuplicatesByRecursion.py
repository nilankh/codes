def RemoveConsecutiveDuplicates(string):
    if len(string)<=1:
        return string
    string2=RemoveConsecutiveDuplicates(string[1:])
    if string[0]==string[1]:
        return string2
    else:
        return string[0]+string2
string=input().strip()
print(RemoveConsecutiveDuplicates(string))
