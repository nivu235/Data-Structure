class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.height=1
    def print(self):
       temp=self.top
       while temp is not None:
           print(temp.value)
           temp=temp.next
a=Stack(10)
a.print()
