class Queue:
    def __init__(self):
        self.__arr = []
        self.__front = 0
        self.__count = 0

    def enqueue(self, ele):
        self.__arr.append(ele)
        self.__count += 1

    def dequeue(self):
        if self.size() == 0:
            return "Queue is Empty!!"
        ele = self.__arr[self.__front]
        self.__front += 1    
        self.__count -= 1  
        return ele  

    def front(self):
        if self.size() == 0:
            return "Queue is Empty!!"
        return self.__arr[self.__front]

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.size() == 0


# Use of Queue
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

print(q.size())
print(q.front())

while not q.isEmpty():
    print(q.dequeue())

print(q.size())
print(q.dequeue())
