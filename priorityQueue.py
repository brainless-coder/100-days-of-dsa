class priorityQueueNode:
    def __init__(self, value, priority) -> None:
        self.value = value
        self.priority = priority

class minPriorityQueue:
    def __init__(self) -> None:
        self.pq = []
    
    def getSize(self):
        return len(self.pq)

    def isEmpty(self):
        return self.getSize() == 0

    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].value

    def __percolateUp(self):
        childIndex = self.getSize()-1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            if self.pq[parentIndex].priority > self.pq[childIndex].priority:
                self.pq[parentIndex], self.pq[childIndex] = self.pq[childIndex], self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break

    def insert(self, value, priority):
        pqNode = priorityQueueNode(value, priority)
        self.pq.append(pqNode)
        self.__percolateUp()
        

    def __percolateDown(self):
        parentIndex = 0
        leftChild, rightChild = 2*parentIndex+1, 2*parentIndex+2
        while leftChild < self.getSize():
            minIdx = parentIndex
            if self.pq[leftChild].priority < self.pq[minIdx].priority:
                minIdx = leftChild
            if rightChild < self.getSize() and self.pq[rightChild].priority < self.pq[minIdx].priority :
                minIdx = rightChild
            if parentIndex == minIdx:
                break
            self.pq[parentIndex], self.pq[minIdx] = self.pq[minIdx], self.pq[parentIndex]
            parentIndex = minIdx
            leftChild, rightChild = 2*parentIndex+1, 2*parentIndex+2

    def removeMin(self):
        if self.isEmpty():
            return None
        x = self.pq[0].value
        self.pq[0] = self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolateDown()
        return x

minPQ = minPriorityQueue()
minPQ.insert('A', 10)
minPQ.insert('C', 5)
minPQ.insert('B', 19)
minPQ.insert('D', 4)
print(minPQ.getMin())
for i in range(4):
    print(minPQ.removeMin())