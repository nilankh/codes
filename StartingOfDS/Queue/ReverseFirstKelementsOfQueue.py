##import queue
##def reverseFirst(q,k):
##    s=[]
##    while(i<k):
##        s.append(queue.queue[0])
##        queue.get()
##    while(len(Stack) != 0):  
##        queue.put(s[-1])  
##        s.pop() 
##        
##    
import queue
def rev(arr, k):
    q = queue.Queue()
    for ele in arr:
        q.put(ele)
    
    s = []
    for i in range(k):
        s.append(q.get())
    while len(s) != 0:
        q.put(s.pop())
    for i in range(q.qsize() - k):
        q.put(q.get())
    while q.empty() is not True:
        print(q.get())
    
arr = [10,20,30,40,50,60,70,80,90]
k = 4
rev(arr, k)
