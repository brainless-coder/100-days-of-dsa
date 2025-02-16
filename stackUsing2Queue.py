import queue

class Stack:
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def push(self, ele):
        self.q1.put(ele)

    def pop(self):
        if (self.size() == 0):
            return "Stack is Empty!!"
        while self.q1.qsize() != 1:
            self.q2.put(self.q1.get())
        ans = self.q1.get()
        while not self.q2.empty():
            self.q1.put(self.q2.get())
        return ans

    def top(self):
        if (self.size() == 0):
            return "Stack is Empty!!"
        while self.q1.qsize() != 1:
            self.q2.put(self.q1.get())
        ans = self.q1.get()
        while not self.q2.empty():
            self.q1.put(self.q2.get())
        self.q1.put(ans)
        return ans

    def size(self):
        return self.q1.qsize()

    def isEmpty(self):
        return self.size() == 0


s = Stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print(s.size())
print(s.isEmpty())
print(s.top())

while not s.isEmpty():
    print(s.pop())

print(s.top())
print(s.isEmpty())
print(s.pop())