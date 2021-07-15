def pairStar(n):
    if len(n)==1:
        return n[0]
    if n[0]==n[1]:
        return n[0]+'*'+pairStar(n[1:])
    else:
        return n[0]+pairStar(n[1:])
n=input()
print(pairStar(n))
