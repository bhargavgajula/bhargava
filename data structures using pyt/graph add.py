def add_node(v):
    global nc
    if v in nodes:
        print(v,"is in graph")
    else:
        nc+=1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp=[]
        for i in range(nc):
            temp.append(0)
        graph.append(temp)
def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"is not present in graph")
    elif v2 not in nodes:
        print(v2,"is not present in graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] =1
        graph[index2][index1] =1
def print_graph():
     for i in range(nc):
           for j in range(nc):
               print(graph[i][j],end=" ")
           print()
graph=[]
nodes=[]
nc=0
print('before adding')
print(nodes)
print(graph)
add_node('A')
add_node('B')
add_node('C')
add_edge("A","B")
add_edge("A","c")
print('After adding')
print(nodes)
print(graph)
print_graph()