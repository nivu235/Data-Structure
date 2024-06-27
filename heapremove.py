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
    def remove(self):
        if len(self.heap)==0:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        maxval=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.sink(0)
        return maxval
    def sink(self,value):
        maxva=value
        while True:
            left=self.left(value)
            right=self.right(value)
            if left<len(self.heap)and self.heap[left]>self.heap[maxva]:
                maxva=left
            if right<len(self.heap) and self.heap[right]>self.heap[maxva]:
                maxva=right
            if maxva!=value:
                self.swap(value,maxva)
                value=maxva
            else:
                 return
            
a=Heap()            
a.insert(99)
a.insert(75)
a.insert(80)
a.insert(55)
a.insert(60)
a.insert(50)
a.insert(65)
print(a.heap)
a.remove()
print(a.heap)
