import queue
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for i in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self,v1,v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def __str__(self):
        return str(self.adjMatrix)

    def __dfsHelper(self, sv, visited):
        print(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] > 0 and visited[i] is False:
                self.__dfsHelper(i, visited)
        
    def dfs(self):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__dfsHelper(i, visited)

    def __bfsHelper(self, sv, visited):
        q = queue.Queue()
        q.put(sv)
        visited[sv] = True
        while q.empty() is False:
            u = q.get()
            print(u)
            for i in range(self.nVertices):
                if self.adjMatrix[u][i] > 0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True
    def bfs(self):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__bfsHelper(i, visited)


    def hasPath(self, v1, v2, visited):
        if self.adjMatrix[v1][v2] > 0:
            return True
        visited[v1] = True
        for i in range(self.nVertices):
            if visited[i] is False:
                if self.adjMatrix[v1][i] > 0 and visited[i] is False:
                    if self.hasPathe(i, v2, visited):
                        return True
        return False
                    
##    def hasPath(self, v1, v2):
##        visited = [False for i in range(self.nVertices)]
##        self.hasPathHelper(v1, v2, visited)
        

##g = Graph(4)
##g.addEdge(0, 1)
##g.addEdge(0, 3)
##g.addEdge(1, 2)
##g.addEdge(2, 3)
##print(g)
##print("*********DFS*********")
##g.dfs()
##print("*********BFS*********")
##g.bfs()
from sys import setrecursionlimit
setrecursionlimit(10000)
li = [int(x) for x in input().split()]
v = li[0]
e = li[1]
c=0
g=Graph(v)
visited = [False for i in range(v)]
for i in range(e):
    a,b=[int(x) for x in input().split()]
    g.addEdge(a,b)
li1 = [int(x) for x in input().split()]
v1 = li1[0]
#print(v1)
v2 = li1[1]
#print(v2)
result = g.hasPath(v1,v2, visited)
if result:
    print("true")
else :
    print("false")
























                
    
