def freqMap(li):
    d = {}
    for num in li:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    return d

def pairSum0(li):
    m = freqMap(li)
    #print(m)
    for num in m:
        #print("inside for num value", num)
        if num >= 0 and -num in m:
            for i in range(0, m[num] * m[-num]):
                #print("i value",i)
                print(-num, num)

n = int(input())
li = [int(i) for i in input().split()]
pairSum0(li)
