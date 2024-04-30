class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Linkedlist:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
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
    def removefirst(self):
        temp=self.head
        pre=temp.next
        self.head=pre
    def removelast(self):
        temp=self.head
        pre=temp.next
        while pre.next is not None:
            temp=temp.next
            pre=pre.next
        self.tail=temp
        temp.next=None
    def removemiddle(self,value):
        if value==0:
            return self.removefirst()
        
        be=self.head
        temp=self.head
        pre=temp.next
        i=0
        for i in range(0,value):
            be=temp
            temp=temp.next
            pre=pre.next
            i=i+1
        be.next=pre
        
    def remove(self,value):
         temp=self.head
         l=0
         while temp is not None:
            l=l+1
            temp=temp.next
         a=l-value
         if a==0:
             temp=self.head
             pre=temp.next
             self.head=pre
         if value==0:
            return self.removefirst()
         else:
            be=self.head
            temp=self.head
            pre=temp.next
            
            for i in range(0,a):
                be=temp
                temp=temp.next
                pre=pre.next
            
            be.next=pre
            return self.head
    
link=Linkedlist(1)
link.append(2)
link.remove(2)

link.print()
