class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
    
    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print(" -> ".join(values))
    def popfirst(self):
        if self.head is None:
            return None
        else:
            pre=self.head
            self.head=pre.next
            self.length-=1
           
    def remove_duplicates(self):
        a=self.head
        v=[]
        valu=[]
        while a is not None:
            valu.append(str(a.value))
            a = a.next
        print(" -> ".join(valu)) 
        
link=LinkedList(1)
link.append(2)
link.append(3)
link.append(4)
link.append(2)
link.append(3)
link.remove_duplicates()
