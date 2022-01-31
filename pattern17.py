'''
*0000*0000*
0*000*000*0
00*00*00*00
000*0*0*000
0000***0000
'''



n=int(input())
i=0
k=2*n
while i<n:
    j=0
    while j<2*n+1:
        if(j==n):
            print('*',end='')
        elif (j==i):
            print('*',end='')
        elif(j==k):
            print('*',end='')
        else:
            print(0,end='')
        j=j+1
    k=k-1
    print()
    i=i+1
