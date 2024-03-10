class Graph:
    def __init__(self):
        self.graph={}
    def add_vertex(self,vertex):
        if vertex in self.graph:
            print("vertex alrady exists")
        else:
            self.graph[vertex]=[]
    def add_edge(self,U,V,W=0):
        if U in self.graph and V in self.graph:
            self.graph[U].append((V,W))
        else:
            print("invalid edge")
    def print_Graph(self):
        for key,items in self.graph.items():
            print(key,"-",items)
    def add_multiple_edges(self,U,*edges):
        if U in self.graph:
            for V,W in edges:
                self.graph[U].append((V,W))
        else:
            print("vertex does not exist")
    def dfs(self,source,visted=None):
        if visted is None:
            visted=[]
        print(source)
        visted.append(source)
        for i in self.graph[source]:
            if i[0] not in visted:
                self.dfs(i[0],visted)
    def bfs(self,source):
        q=[]
        ans=[]
        q.append(source)
        while q:
            source=q.pop(0)
            for i in self.graph[source]:
                if i[0] not in ans:
                    ans.append(i[0])
                    q.append(i[0])
        print(*ans)
    def dijistras(self,source,destination):
        



        

g=Graph()
g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')
g.add_edge('a','b',5)
g.add_edge('a','d',1)
g.add_edge('b','c',4)
g.add_edge('b','d',3)
g.add_edge('d','c',3)
g.add_edge('c','a',3)
g.print_Graph()
g.dfs('a')
g.bfs('a')