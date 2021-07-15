##def longestConsecutiveSubsequence(l):
##    m = {l[i]:i for i in range(len(l)-1, -1, -1)}
##    print(m)
##    visited = {}
##    start, end = l[0], l[0]
##    startM, endM = start, end
##    for num in l:
##        if num not in visited:
##            visited[num] = True
##            start, end = num, num
##        while start-1 in m:
##            start -= 1
##            visited[start] = True
##        while end+1 in m:
##            end += 1
##            visited[end] = True
##        if (endM-startM+1 < end-start+1) or ((endM-startM+1 == end-start+1) and (m[start] < m[startM])):
##            startM, endM = start, end
##    return startM, endM
 
##n=int(input())
##l=list(int(i) for i in input().strip().split(' '))
##st,final = longestConsecutiveSubsequence(l)
##for num in range(st,final+1):
##    print(num)


n=int(input())
arr=[int(i) for i in input().split()]
d={}
for i in arr:
	d[i]=0
	print(d)
ans=[]
for i in range(len(arr)):
    print("for loop ith value", i)
    an=[]
    if d[arr[i]]==1:
            
	    continue
    print("arr[i]-1", arr[i] - 1)
    if arr[i]-1 not in d:
            
	    z=arr[i]
	    print("chala ye ", i)
	    print("z value", z)
	    while (z in d) and (d[z]==0):
		    # an+=1
		    d[z]=1
		    an.append(z)
		    print("while loop z vaue",z)
		    z+=1
    if len(an)>len(ans):
    	ans=an
    	print("answer=an", ans)
for i in ans:
        #print("Last for loop chala", i)
	print(i)







	


















    
