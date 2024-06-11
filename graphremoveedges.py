class Graph:
    def __init__(self):
        self.adj_list={}
    def addvertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex]=[]
            return True
        return False
    def addedge(self,v1,v2):
        if v1 in self.adj_list.keys()and v1 in self.adj_list.keys():
           self.adj_list[v1].append(v2)
           self.adj_list[v2].append(v1)
           return True
        return False
    def print(self):
        for vertex in self.adj_list:
            print(vertex,":",self.adj_list[vertex])
    def removedge(self,v1,v2):
        if v1 in self.adj_list.keys()and v1 in self.adj_list.keys():
           try: 
               self.adj_list[v1].remove(v2)
               self.adj_list[v2].remove(v1)
           except ValueError:
               pass
           return True
        return False
a=Graph()
a.addvertex("A")
a.addvertex("B")
a.addvertex("C")
a.addvertex("D")
a.addedge("A","B")
a.addedge("B","C")
a.addedge("C","A")
a.removedge("A","D")
a.removedge("A","B")
a.print()

            
