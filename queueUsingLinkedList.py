class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.__front = None
        self.__rear = None
        self.__count = 0

    def enqueue(self, ele):
        newNode = Node(ele)
        if self.__front is None:
            self.__front = self.__rear = newNode
        else:
            self.__rear.next = newNode
            self.__rear = self.__rear.next
        self.__count += 1

    def dequeue(self):
        if self.__front is None:
            return "Queue is Empty!!"
        ans = self.__front.data
        self.__front = self.__front.next
        self.__count -= 1
        return ans

    def front(self):
        if self.__front is None:
            return "Queue is Empty!!"
        return self.__front.data

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

print(q.isEmpty())
print(q.dequeue())
