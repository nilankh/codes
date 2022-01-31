N = int(input())


i = 0
N1 = 0
N2 = 1
while(i < N):
    if(i <= 1):
        Nth = i
    else:
        Nth = N1+N2
        N1=N2
        N2=Nth
           
    i = i + 1

    
    print(Nth,end=",")
