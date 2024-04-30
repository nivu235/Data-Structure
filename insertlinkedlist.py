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
    def prepand(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            temp=self.head    
            self.head=new_node
            self.head.next=temp
        self.length+=1    
    def get(self,index):
        if index<0 or index>self.length:
            return None
        else:
           temp=self.head
           for i in range(index):
               temp=temp.next
           return temp
    def set_value(self,index,value):
        if index<0 or index>self.length:
            return None
        else:
           temp=self.head
           for i in range(index):
               temp=temp.next
           temp.value=value
    def insert(self,index,value):
        if index<0 or index>self.length:
            return None
        if index==0:
            return sef.prepand(value)
        if index==self.length:
            return self.append(value)
        new_node=Node(value)
        temp=self.get(index-1)
        
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
link=LinkedList(1)
link.append(2)
link.append(3)
link.append(4)
link.insert(2,5)
link.print()
