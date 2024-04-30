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
    def popfirst(self):
        if self.head is None:
            return None
        else:
            pre=self.head
            self.head=pre.next
            self.length-=1
    def pop(self):
        if self.head is None:
            return None
        else:
            temp=self.head
            pre=self.head
            while temp.next is not None:
                temp=temp.next
                pre=temp
            self.tail=pre
            pre.next=None
            self.length-=1
            
    def get(self,index):
        if index<0 or index>self.length:
            return None
        else:
           temp=self.head
           for i in range(index):
               temp=temp.next
           return temp
    def remove(self,index):
       if self.head is None:
            return None
       if index==0:
           return self.popfirst()
       if index==self.length:
           return self.pop()
       temp=self.get(index-1)
       pre=self.get(index)
       temp.next=pre.next
       self.length-=1
link=LinkedList(1)
link.append(2)
link.append(3)
link.append(4)
link.remove(1)
link.print()
