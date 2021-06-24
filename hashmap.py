class MapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Map:
    def __init__(self):
        self.bucketSize = 5
        self.buckets = [None for i in range(self.bucketSize)]
        self.count = 0

    def size(self):
        return self.count

    def getBucketIndex(self, hc):
        return abs(hc) % self.bucketSize

    def rehash(self):
        self.bucketSize *= 2
        temp = self.buckets
        self.buckets = [None for i in range(self.bucketSize)]
        self.count = 0
        for i in range(len(temp)):
            head = temp[i]
            while head is not None:
                self.insert(head.key, head.value)
                head = head.next

    def getLoadFactor(self):
        return self.count/self.bucketSize

    def insert(self, key, value):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        head = self.buckets[index]
        newNode = MapNode(key, value)
        newNode.next = head
        self.buckets[index] = newNode
        self.count += 1
        if self.getLoadFactor() >= 0.7:
            self.rehash()

    def search(self, key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return "Element is not present"

    def delete(self, key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        prev = None
        while head is not None:
            if head.key == key:
                if prev is None:
                    self.buckets[index] = head.next
                else:
                    prev.next = head.next
                    head.next = None
                self.count -= 1
                return head.value
            prev = head
            head = head.next
        return "Element not found"


m = Map()
for i in range(10):
    m.insert("abc" + str(i), i+1)
    print(m.getLoadFactor())

for i in range(10):
    print("abc" + str(i) + ": ", m.search("abc" + str(i)))

# m.insert("Prime", 55)
# print(m.getLoadFactor())
# # print(m.size())
# m.insert("Loki", 94)
# print(m.getLoadFactor())
# # print(m.size())
# m.insert("Primey", 60)
# print(m.getLoadFactor())
# m.insert("Thor", 60)
# print(m.getLoadFactor())
# m.insert("Hulk", 60)
# print(m.getLoadFactor())
# m.insert("Tony", 60)
# print(m.getLoadFactor())
# m.insert("Steve", 60)
# print(m.getLoadFactor())
# print(m.size())
# print(m.search("Prime"))
# print(m.search("Loki"))
# print(m.search("Thor"))
# print(m.delete("Prime"))
# print(m.delete("Thor"))
# print(m.search("Prime"))