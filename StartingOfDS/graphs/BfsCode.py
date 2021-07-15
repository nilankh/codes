import queue
class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(nVertices)]for j in range(nVertices)]
        
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1

    def removeEdge(self,v1,v2):
        if self.containsEdge(v1,v2) is False:
            return
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0

    def containsEdge(self,v1,v2):
        return True if self.adjMatrix[v1][v2]>0 else False

    def __str__(self):
        return str(self.adjMatrix)

    def __bfsHelper(self, sv, visited):
        q=queue.Queue()
        q.put(sv)
                #print(visited)
        visited[sv]=True
        while q.empty() is False:
            u=q.get()
            print(u, end = ' ')
            for i in range(self.nVertices):
                #print("ith value",i)
                if self.adjMatrix[u][i]>0 and visited[i] is False:

                    q.put(i)
                    #print(q)
                    visited[i]=True
    def bfs(self):
        visited=[False for i in range(self.nVertices)]
        print(visited)
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__bfsHelper(i, visited)
        
    

##g=Graph(5)
##g.addEdge(0,1)
##g.addEdge(1,3)
##g.addEdge(2,4)
##g.addEdge(2,3)
##g.addEdge(0,2)
##g.bfs()
#print(g)
    
li = [int(x) for x in input().split()]
v = li[0]
e = li[1]
g = Graph(v)
for i in range(e):
    a, b = [int(x) for x in input().split()]
    g.addEdge(a, b)
g.bfs()







