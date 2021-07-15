import queue
class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(nVertices)]for i in range(nVertices)]

    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1

    def removeEdge(self,v1,v2):
        if self.containsEdge(v1,v2) is False:
            return
        self.adjMatrix[v1][v2]=0
        sefl.adjMatrix[v2][v1]=0

    def containsEdge(self,v1,v2):
        return True if self.adjMatrix[v1][v2]>0 else False

    def __str__(self):
        return str(self.adjMatrix)

    def bfsHelper(self,sv,ev):
        parent = {}
        path = []
        visited = [False for i in range(self.nVertices)]
        q = queue.Queue()
        q.put(sv)
        while not(q.empty()):
            curr = q.get()
            visited[curr] = True
            for i in range(self.nVertices):
                if self.adjMatrix[curr][i] > 0 and visited[i] is False:
                    parent[i] = curr
                    visited[i] = True
                    q.put(i)
                    if ev == i:
                        path.append(i)
                        while not(q.empty()):
                            rem = q.get()
                        break
        j = ev
        while j in parent.keys():
            path.append(parent[j])
            j = parent[j]
        
        return path
                                    
                                        
                                        
li = [int(x) for x in input().split()]
v = li[0]
e = li[1]
g=Graph(v)
for i in range(e):
    a,b=(int(x) for x in input().split())
    g.addEdge(a,b)
a,b=(int(x) for x in input().split())

print(*g.bfsHelper(a,b),end=" ")
