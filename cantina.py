import numpy as np

class Conn:
    def __init__(self, node) -> None:
        self.dest = node
        self.visited = False

class Node:
    def __init__(self, ind):
        self.ind = ind
        self.neighbors = []
        self.onStack = False
        self.visited = False


    def __repr__(self) -> str:
        nbh = []
        for nb in self.neighbors:
            nbh.append((self.ind, nb.dest.ind, nb.visited))
        return str((self.ind, str(nbh)))

    def next(self):
        for nb in self.neighbors:
            _, visited = nb
            if not visited:
                return nb
        return None

class Graph:
    def __init__(self) -> None:
        self.nodes = {}

    def __repr__(self) -> str:
        return str(self.nodes)

    def stronglyConnectedComponents(self):
        node = self.nodes[0]
        node.parent = 0
        node.onStack = True
        node.component = 0
        self.scc(node)

    def scc(self, node):
        node.visited = True
        node.onStack = True
        next, _ = node.next()
        if not next: return
        # node.
        if next.onStack:
            if next.component <= node.component:
                next.onStack = False
                par = node.parent
                while par != node:
                    par.onStack = False
                    par = node.parent
        else:
            next.parent = node
            next.component = node.component+1

        self.scc(next)


n = int(input())
languages = set()
cantina = []
G = Graph()
for i in range(n):
    member = input().split()
    cantina.append(member[1:])
    node = Node(i)
    G.nodes[i] = node
    for lang in member[1:]:
        languages.add(lang)

languages = list(languages)
L = len(languages)
languages = { languages[i] : i for i in range(len(languages)) }
understands = [[] for _ in range(L)] 

for i in range(n):
    for l in cantina[i]:
        lang = languages[l]
        understands[lang].append(i)

for i in range(n):
    speaks = languages[cantina[i][0]]
    node = G.nodes[i]
    for u in understands[speaks]:
        if i != u:
            node.neighbors.append(Conn(G.nodes[u]))

# G.stronglyConnectedComponents()
print(G)
