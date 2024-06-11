class Graph:
    def __init__(self):
        self.adj_list={}
    def addvertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex]=[]
            return True
        return False
    def addedge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def printgraph(self):
        for vertex in self.adj_list:
            print(vertex,":",self.adj_list[vertex])
a=Graph()
a.addvertex("A")
a.addvertex("B")
a.addedge("A","B")
a.printgraph()
            
