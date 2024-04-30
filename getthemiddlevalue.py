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
   
       
            
    def find_middle_node(self):
        temp=self.head
        i=0
        length=0
        while temp is not None:
            length+=1
            temp=temp.next
          
        if length%2!=0:
            index=length/2
            i=int(index)
            
        else:
            length%2==0
            index=length/2
            i=int(index)
            
        temp=self.head
        for i in range(i):
            temp=temp.next
        return temp
   


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


print( my_linked_list.find_middle_node().value )
#def find_middle_node(self):
 #       slow = self.head
  #      fast = self.head
   #     while fast is not None and fast.next is not None:
    #        slow = slow.next
     #       fast = fast.next.next
      #  return slow\\

        
