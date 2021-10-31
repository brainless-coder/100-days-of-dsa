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
        while True:
            leftChild, rightChild = 2*parentIndex+1, 2*parentIndex+2
            if rightChild < self.getSize():
                if self.pq[parentIndex].priority > self.pq[leftChild].priority and self.pq[leftChild].priority < self.pq[rightChild].priority:
                    self.pq[parentIndex], self.pq[leftChild] = self.pq[leftChild], self.pq[parentIndex]
                    parentIndex = leftChild
                elif self.pq[parentIndex].priority > self.pq[rightChild].priority and self.pq[rightChild].priority < self.pq[leftChild].priority:
                    self.pq[parentIndex], self.pq[rightChild] = self.pq[rightChild], self.pq[parentIndex]
                    parentIndex = rightChild
                else:
                    break
            elif leftChild < self.getSize():
                if self.pq[parentIndex].priority > self.pq[leftChild].priority:
                    self.pq[parentIndex], self.pq[leftChild] = self.pq[leftChild], self.pq[parentIndex]
                break

    def removeMin(self):
        x = self.pq[0].value
        self.pq[0] = self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolateDown()
        return x
