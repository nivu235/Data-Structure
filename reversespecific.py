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
    def reverse(self):
        temp=self.head
        for i in range(2,4):
            print(temp.value)
            temp=temp.next
             
link=LinkedList(1)
link.append(2)
link.append(3)
link.append(4)
link.append(5)
link.reverse()

