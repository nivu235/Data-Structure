class Heap:
    def __init__(self):
        self.heap=[]
    def left(self,index):
        return 2*index+1
    def right(self,index):
        return 2*index+2
    def parent(self,index):
        return (index-1)//2
    def swap(self,index1,index2):
        self.heap[index1],self.heap[index2]=self.heap[index2],self.heap[index1]
    def insert(self,value):
        self.heap.append(value)
        current=len(self.heap)-1
        while current>0 and self.heap[current]>self.heap[self.parent(current)]:
            self.swap(current,self.parent(current))    
            current=self.parent(current)
a=Heap()
a.insert(99)
a.insert(61)
a.insert(58)
a.insert(72)
print(a.heap)
a.insert(100)
print(a.heap)
