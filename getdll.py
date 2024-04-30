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
        self.length=1
    def append(self,value):
        new_node=Node(value)
        temp=self.head
        if temp is None:
            self.head=new_node
            self.tail=new_node
            self.length
        else:
            self.tail.next=new_node
            new_node.pre=self.tail
            self.tail=new_node
            self.length+=1
    def get(self,index):
        if index < 0 or index > self.length:
            return None
        else:
            temp=self.head
            for _ in range(index):
                temp=temp.next
            return temp.value
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
print(a.get(2))
a.print()
