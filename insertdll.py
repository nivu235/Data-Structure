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
    def prepend(self,value):
        new_node=Node(value)
        temp=self.head
        if temp is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.head.pre=new_node
            new_node.next=self.head
            self.head=new_node
    def insert(self,pos,value):
        new_node=Node(value)
        temp=self.head
        pre=temp.next
        if pos==0:
            return self.prepend(value)
        for _ in range(pos-1):
            temp=temp.next
        new_node.pre=temp
        new_node.next=temp.next
        temp.next=new_node
    def print(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
a=DLL(1)
a.append(2)
a.append(3)
a.append(4)
a.insert(0,5)
a.print()
