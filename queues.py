import queue

def reverseRec(q):
    if q.empty():
        return
    a = q.get()
    reverseRec(q)
    q.put(a)

def kreverseOpti(q, k, n):
    if k == 0:
        return q
    a = q.get()
    kreverseOpti(q, k-1, n)
    q.put(a)
    if q.qsize() == n:
        i = 0
        while i < n-k:
            q.put(q.get())
            i += 1

q = queue.Queue()
s = input().split()
n, k = int(s[0]), int(s[1])
li = [q.put(int(x)) for x in input().split()]
# reverseRec(q)
# kReverse(q, k)
kreverseOpti(q, k, n)
while not q.empty():
    print(q.get(), end=" ")
