class Edge:
    def __init__(self, src, dest, wt):
        self.src = src
        self.dest = dest
        self.wt = wt


def getParent(v, parent):
    if v == parent[v]:
        return v
    return getParent(parent[v], parent)

def kruskal(edges, nVertices):
    parent = [i for i in range(nVertices)]
    edges = sorted(edges, key= lambda edge: edge.wt)
    count, i = 0, 0
    output = []

    while count < nVertices-1:
        currentEdge = edges[i]
        srcParent = getParent(currentEdge.src, parent)
        destParent = getParent(currentEdge.dest, parent)
        if srcParent != destParent:
            output.append(currentEdge)
            count += 1
            parent[srcParent] = destParent      # changing topmost parent
        i += 1

    return output


s = input().split()
n, E = int(s[0]), int(s[1])
edges = []
for i in range(E):
    curr_input = input().split()
    src, dest, wt = int(curr_input[0]), int(curr_input[1]), int(curr_input[2])
    edge = Edge(src, dest, wt)
    edges.append(edge)

output = kruskal(edges, n)

for edge in output:
    if edge.src < edge.dest:
        print(f"{edge.src} {edge.dest} {edge.wt}")
    else:
        print(f"{edge.dest} {edge.src} {edge.wt}")
