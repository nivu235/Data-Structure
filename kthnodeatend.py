#kth value
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
   
def find_kth_from_end(self,k):
        temp=self.head
        i=0
        length=0
        while temp is not None:
            length+=1
            temp=temp.next
        a=length-k
        temp=self.head
        for i in range(a):
            temp=temp.next
        return temp    
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
k = 1
result=find_kth_from_end(my_linked_list,k)
print(result.value)
