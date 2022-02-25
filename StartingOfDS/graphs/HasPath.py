
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
    def __hasPathHelper(self,visited,v1,v2):
        global c
        
        visited[v1] = True
        for i in range(self.nVertices):
            #print("1st i", i)
            if self.adjMatrix[v1][i] > 0 and visited[i] is False :
                #print("value of ith before recursion", i)
                self.__hasPathHelper(visited,i,v2)
                #print("value of ith after recursion", i)
                if i==v2:
                    c = 1
                    #return c(ye automatic c = 1 return ho jyga dnt wry)
        return c
    def hasPath(self,v1,v2):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                
                p=self.__hasPathHelper(visited,v1,v2)
        return p
    #correct too
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

li = [int(x) for x in input().split()]
v = li[0]
e = li[1]
c=0
g=Graph(v)
for i in range(e):
    a,b=[int(x) for x in input().split()]
    g.addEdge(a,b)
li1 = [int(x) for x in input().split()]
v1 = li1[0]
#print(v1)
v2 = li1[1]
#print(v2)
result = g.hasPath(v1,v2)
if result ==1:
    print("true")
else :
    print("false")









    

