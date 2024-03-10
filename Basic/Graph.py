vertices=input("Enter vertices(As space separated)").split()
graph={}
if vertices[0].isdigit():
    vertices=map(int,vertices)
for i in vertices:
    graph[i]=[]
while True:
    edges=input("enter edge:(vertex1->vertex2) or Enter .exit to exit")
    if edges==".exit":
        break
    if edges[0].isdigit():
        vertex1,vertex2=map(int,edges.split())
    else:
        vertex1,vertex2=edges.split()
    if vertex1 not in graph or vertex2 not in graph:
        print("Invalid input vertices you entered are not present in the graph..!")
    else: 
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)
print(graph)
visted=set()
def dfs(source,graph,visted):
    visted.add(source)
    print(source,end=" ")
    for nodes in graph[source]:
        if nodes not in visted:
            dfs(nodes,graph,visted)
dfs('a',graph,visted)

    


