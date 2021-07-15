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
        sefl.adjMatrix[v2][v1]=0

    def containsEdge(self,v1,v2):
        return True if self.adjMatrix[v1][v2]>0 else False
    
    def __str__(self):
        return str(self.adjMatrix)

    def __isConnectedHelper(self,sv,visited):
        #print(sv)
        visited[sv]=True
        for i in range(self.nVertices):
            if(self.adjMatrix[sv][i]>0 and visited[i] is False):
                self.__isConnectedHelper(i,visited)

    def isConnected(self):
        visited=[False for i in range(self.nVertices)]
        count=0
        for i in range(self.nVertices):
            if visited[i] is False:
                count+=1
                self.__isConnectedHelper(i,visited)
        if count==1:
            return True
        else:
            return False
                
li = [int(x) for x in input().split()]
v = li[0]
e = li[1]

g=Graph(v)
for i in range(e):
    a,b=[int(x) for x in input().split()]
    g.addEdge(a,b)
result = g.isConnected()
if result:
    print("true")
else :
    print("false")

    
