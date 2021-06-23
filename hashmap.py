class MapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Map:
    def __init__(self):
        self.bucketSize = 10
        self.buckets = [None for i in range(self.bucketSize)]
        self.count = 0

    def size(self):
        return self.count

    def getBucketIndex(self, hc):
        return abs(hc) % self.bucketSize

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
                    head = prev
                    del head
                else:
                    prev.next = head.next
                    head.next = None
                self.count -= 1
                return "Element successfully deleted"
            prev = head
            head = head.next
        return "Element not found"


m = Map()
m.insert("Prime", 55)
print(m.size())
m.insert("Loki", 94)
print(m.size())
m.insert("Prime", 60)
print(m.size())
print(m.search("Prime"))
print(m.search("Loki"))
print(m.search("Thor"))
print(m.delete("Prime"))
print(m.size())
print(m.delete("Thor"))
print(m.size())
print(m.search("Prime"))