class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.height=1
    def push(self,value):
        new_node=Node(value)
        temp=self.top
        if temp is None:
            self.top=new_node
        else:
            new_node.next=temp
            self.top=new_node
            self.height+=1
    def print(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next
a=Stack(1)
a.push(2)
a.push(3)
a.print()
