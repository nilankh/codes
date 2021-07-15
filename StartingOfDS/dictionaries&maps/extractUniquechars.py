
##tried by my own
##def uniqueChar(s):
##    string = ''
##    dict = {}
##    for char in s:
##        if char in dict:
##            dict[char] += 1
##        else:
##            dict[char] = 1
##    for key in dict:
##        print(key,end='')
####    print(dict)
##
##s = input()
##uniqueChar(s)


def uniqueChar(s):
    ans = ''
    m = {}
    for char in s:
##        print("char",char)
        if char not in m:
##            print("m",m)
            ans = ans + char
##            print("inside ans ",ans)
            m[char] = True
##            print(m)
    return ans

s = input()
print(uniqueChar(s))






##def uniqueChars(string):
##    # Please add your code here
##    
##    d={}
##    for w in string:
##        d[w]=d.get(w,0)+1
##        print("firsr for",d)
##    for ele in d:
##        print("ele",ele)
##        d[ele]=1
##        print("second d",d)
##    x=""
##    for w in string:
##        
##        for i in range(d[w]):
##            print("inside",w)
##            print(w,end="")
##        d[w]=0
### Main
##string = input()
##uniqueChars(string)







