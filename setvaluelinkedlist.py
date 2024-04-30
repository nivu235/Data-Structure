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
    def print(self):
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
    def get(self,index):
        if index<0 or index>self.length:
            return None
        else:
           temp=self.head
           for i in range(index):
               temp=temp.next
           return temp.value
    def set_value(self,index,value):
        if index<0 or index>self.length:
            return None
        else:
           temp=self.head
           for i in range(index):
               temp=temp.next
           temp.value=value
               
link=LinkedList(1)
link.append(2)
link.append(3)
link.append(4)
print(link.get(3))
link.set_value(3,5)
link.print()

        
