import numpy as np

class Conn:
    def __init__(self, node) -> None:
        self.dest = node
        self.visited = False

class Node:
    def __init__(self, ind, name):
        self.ind = ind
        self.name = name
        self.neighbors = []
        self.onStack = False
        self.visited = False
        self.component = -1


    def __repr__(self) -> str:
        nbh = []
        for nb in self.neighbors:
            nbh.append((self.ind, nb.dest.ind, nb.visited))
        return str((self.name, f'comp: {self.component}', str(nbh))) + '\n'

    def next(self):
        for nb in self.neighbors:
            if not nb.visited:
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
        nb = node.next()
        if not nb: return
        nb.visited = True
        next = nb.dest
        if next.onStack:
            if next.component <= node.component:
                node.onStack = False
                nextComp = next.component
                node.component = nextComp
                par = node.parent
                while par != next:
                    par.onStack = False
                    par.component = nextComp
                    par = par.parent
        else:
            next.parent = node
            if next.component < 0:
                next.component = node.component+1

        self.scc(next)


n = int(input())
languages = set()
cantina = []
G = Graph()
for i in range(n):
    member = input().split()
    cantina.append(member[1:])
    node = Node(i, member[0])
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

G.stronglyConnectedComponents()
print(G)
