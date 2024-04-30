class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
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
def add(l1,l2):
    link3=LinkedList()
    h1=l1.head
    h2=l2.head
    while h1 and h2 is not None:
        a=h1.value+h2.value
        link3.append(a)
        h1=h1.next
        h2=h2.next
    link3.printl()     
link=LinkedList()
link.append(5)
link.append(10)
link.append(15)
link.printl()
link2=LinkedList()
link2.append(2)
link2.append(3)
link2.append(30)
link2.printl()
link3=add(link,link2)




