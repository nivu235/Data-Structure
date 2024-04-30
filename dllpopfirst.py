class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.pre=None
class DLL:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
    def append(self,value):
        new_node=Node(value)
        temp=self.head
        if temp is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.pre=self.tail
            self.tail=new_node
    
    def popf(self):
        temp=self.head
        self.head=temp.next
        self.head.pre=None
        temp.next=None
    def print(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
a=DLL(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.append(6)
a.popf()
a.print()
