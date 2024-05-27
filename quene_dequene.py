class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Quene:
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1
    def enquene(self,value):
        new_node=Node(value)
        temp=self.first
        if temp is None:
            self.first=new_node
            self.last=new_node
        else:
            self.last.next=new_node
            self.last=new_node
            self.length+=1
    def dequene(self):
        if self.length==1:
            self.first=None
            self.last=None
        else:
            temp=self.first
            self.first=temp.next
            temp=None
    def print(self):
        temp=self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next
a=Quene(1)
a.enquene(2)
a.enquene(3)
a.enquene(4)
a.dequene()
a.dequene()
a.print()
            
