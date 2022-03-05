import queue
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def __str__(self):
        return str(self.adjMatrix)

    def __hasPathByBFShelper(self, sv, ev, visited):
        if sv == ev:
            return True

        q = queue.Queue()
        q.put(sv)
        visited[sv] = True
        while q.empty() is False:
            u = q.get()
            #print("U data", u)
            for i in range(self.nVertices):
                #print("I value inside for loop,", i)
                if(self.adjMatrix[u][i] == 1 and not visited[i]):
                    #print("ith value inside for loop",i)
                    if i == ev:
                        #print("ith value",i)
                        return True
                    q.put(i)
                    #print("q",q)
                    visited[i] = True
                    #print("Every time visited", visited)
        return False

    def hasPathByBFS(self, sv, ev):
        visited = [False for i in range(self.nVertices)]
        #k = self.__hasPathByBFShelper(sv, ev, visited)
        #print(k)
        #return k
        for i in range(self.nVertices):
            if visited[i] is False:
                
                return self.__hasPathByBFShelper(sv, ev, visited)

li = [int(x) for x in input().split()]
v = li[0]
e = li[1]
g = Graph(v)
for i in range(e):
    a,b=[int(x) for x in input().split()]
    g.addEdge(a,b)
li = [int(x) for x in input().split()]
sv = li[0]
ev = li[1]

if g.hasPathByBFS(sv, ev):
    print('true')
else:
    print('false')



    
