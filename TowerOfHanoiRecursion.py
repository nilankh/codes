
def towerOfHanoi(n,a,b,c):
    if n==1:
        print("MOVE 1ST DISK FROM ",a,"TO",c)
        return
    towerOfHanoi(n-1,a,c,b)
    print("MOVE",n," DISK FROM ",a,"TO",c)
    towerOfHanoi(n-1,b,a,c)
n=int(input())
towerOfHanoi(n,'s','h','d')
'''

def th(n,a,b,c):
    if n==1:
        print("MOVE 1STDISK FROM",a,"to",c)
        return
    th(n-1,a,c,b)
    print("MOVE ",n,"DISK FROM ",a,"TO",c)
    th(n-1,b,a,c)
th(4,'a','b','c')
'''
