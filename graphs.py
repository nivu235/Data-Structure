class Graph:
    def __init__(self):
        self.adj_list={}
    def addvertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex]=[]
            return True
        else:
            return False
    def printgra(self):
        for vertex in self.adj_list:
            print(vertex,":",self.adj_list[vertex])
            
a=Graph()
a.addvertex("A")
a.printgra()
