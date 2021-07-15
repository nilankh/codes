import queue
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __str__(self):
        return str(self,adjMatrix)
##    def __h(self, sv, ev, visited):
##        parent = {}
##        q = queue.Queue()
##        if self.adjMatrix[sv][ev] == 1 and sv == ev:
##            ans = []
##            ans.append(sv)
##            return ans
##        q.put(sv)
##        visited[sv] = True
##        while q.empty() if False:
##            u = q.get()
##            for i in range(self.nVertices):
##                if(self.adjMatrix[u][i] > 0 and visited[i] is False):
##                    parent[i] = u
##                    q.put(i)
##                    visited[i] = True
    def __getPathByBFShelper(self, sv, ev, visited):
        parent = {}
        q = queue.Queue()
        if self.adjMatrix[sv][ev] == 1 and sv == ev:
            ans = []
            ans.append(sv)
            return ans
        q.put(sv)
        visited[sv] = True
        while q.empty() is False:
            u = q.get()
            for i in range(self.nVertices):
                if(self.adjMatrix[u][i] > 0 and visited[i] is False):
                    parent[i] = u
                    q.put(i)
                    visited[i] = True
                    if i == ev:
                        ans = []
                        ans.append(ev)
                        value = parent[ev]

                        while value != sv:
                            ans.append(value)
                            value = parent[value]
                        ans.append(value)
                        return ans
        return []
    def getPathByBFS(self, sv, ev):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                return self.__getPathByBFShelper(sv, ev, visited)

li = [int(x) for x in input().split()]
v = li[0]
e = li[1]
g = Graph(v)
for i in range(e):
    a, b = [int(x) for x in input().split()]
    g.addEdge(a, b)
li1 = [int(x) for x in input().split()]
sv = li1[0]
ev = li1[1]

li = g.getPathByBFS(sv, ev)
if len(li) != 0:
    for element in li:
        print(element, end = ' ')
        



        
