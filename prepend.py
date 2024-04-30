class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    def printl(self):
       temp=self.head
       while temp is not None:
           print(temp.value)
           temp=temp.next
    def append(self,value):
       new_node=Node(value)
       if self.head is None:
          self.head=new_node
          self.tail=new_node
       else:
           self.tail.next=new_node
           self.tail=new_node
       self.length+=1
    def prepend(self,value):
        new_node=Node(value)
        pre=self.head
        self.head=new_node
        self.head.next=pre
        self.length+=1
link=LinkedList(1)
link.append(2)
link.append(3)
link.prepend(4)
link.prepend(5)
print(link.head.value)
print(link.tail.value)
link.printl()
