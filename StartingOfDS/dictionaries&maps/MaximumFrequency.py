##def maxFreq(l):
##    d={}
##    for w in l:
##        d[w]=d.get(w,0)+1
##    freq = 0
##    ans = 0
##    for w in d:
##        if d[w] > freq:
##            freq = d[w]
##            ans = w
##        elif d[w] == freq:
##            freq = d[w]
##            if l.index(w) < l.index(ans):
##                ans = w
##    return ans
##
### Main
##n=int(input())
##l=list(int(i) for i in input().strip().split(' '))
##print(maxFreq(l))


def maxFreq(l):
    d = {}
    for num in l:
##      print("num",num)
        if num in d:
            d[num] += 1
##          print("inside if",d[num])
##          print("inside",d)
        else:
            d[num] = 1
##            print("inside else",d[num])
##            print("else",d)
##  print(d)
    ans = l[0]
##  print(ans)
    for num in l:
        if d[num] > d[ans]:
            ans = num
##          print("answer",ans)
    return ans

n = int(input())
li = [int(x) for x  in input().split()]
print(maxFreq(li))




























        
