class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def push(self, element):
        newNode = Node(element)
        newNode.next = self.__head
        self.__head = newNode
        self.__count += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty!!"
        temp = self.__head
        self.__head = self.__head.next
        temp.next = None
        ans = temp.data
        del temp
        self.__count -= 1
        return ans

    def top(self):
        if self.isEmpty():
            return "Stack is Empty!!"
        return self.__head.data

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

    
    