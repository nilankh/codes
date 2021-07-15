import queue
class StackUsingQueues:
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def push(self,data):
        self.q1.put(data)

    def pop(self):
        while self.q1.qsize()>1:
            self.q2.put(self.q1.get())
        ans=self.q1.get()
        self.q1,self.q2=self.q2,self.q1
        return ans

    def top(self):
        while self.q1.qsize()>1:
            self.q2.put(self.q1.get())
        ans=self.q1.get()
        self.q2.put(ans)
        self.q1,self.q2=self.q2,self.q1

        return ans

    def getSize(self):
        return self.q1.qsize()
s = StackUsingQueues()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

#while s.q1.qsize()!=0:
#    print(s.q1.get(),end=' ')
print(s.top())        





    

