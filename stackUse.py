# from stackUsingArray import Stack
# from stackUsingLL import Stack
import queue

# s = Stack()

# s.push(10)
# s.push(20)
# s.push(30)

# while s.isEmpty() is False:
#     print(s.pop())

# print(s.top())


# Inbuit Stack as List
# s = [1, 2, 3]

# s.append(4)     # Push
# s.append(5)

# print(s.pop())     # Pop
# print(s.pop())

# print(s[len(s) - 1])    # top
# print(len(s))           # size

# Inbuit Queue
q = queue.Queue()

q.put(1)
q.put(2)
q.put(3)
print(q.qsize())


while not q.empty():
    print(q.get())

# Queue as Stack
q = queue.LifoQueue()

q.put(1)
q.put(2)
q.put(3)

print(q.qsize())

while not q.empty():
    print(q.get())


