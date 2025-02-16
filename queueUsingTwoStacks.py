from stackUsingArray import Stack

class Queue1:
    def __init__(self):
        self.__s1 = Stack()
        self.__s2 = Stack()

    def enqueue(self, ele):
        self.__s1.push(ele)

    def dequeue(self):
        if self.size() == 0:
            return "Queue is Empty"
        while self.size() > 1:
            self.__s2.push(self.__s1.pop())
        ans = self.__s1.pop()
        while not self.__s2.isEmpty():
            self.__s1.push(self.__s2.pop())
        return ans
    
    def front(self):
        if self.size() == 0:
            return "Queue is Empty"
        while not self.__s1.isEmpty():
            self.__s2.push(self.__s1.pop())
        ans = self.__s2.top()
        while not self.__s2.isEmpty():
            self.__s1.push(self.__s2.pop())
        return ans

    def size(self):
        return self.__s1.size()

    def isEmpty(self):
        return self.size() == 0


class Queue2:
    def __init__(self):
        self.__s1 = Stack()
        self.__s2 = Stack()

    def enqueue(self, ele):
        while not self.__s1.isEmpty():
            self.__s2.push(self.__s1.pop())
        self.__s1.push(ele)
        while not self.__s2.isEmpty():
            self.__s1.push(self.__s2.pop())

    def dequeue(self):
        if self.size() == 0:
            return "Queue is Empty"
        return self.__s1.pop()

    def front(self):
        if self.size() == 0:
            return "Queue is Empty"
        return self.__s1.top()

    def size(self):
        return self.__s1.size()

    def isEmpty(self):
        return self.size() == 0


# Use of Queue
# q = Queue1()
q = Queue2()
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
print(q.front())
