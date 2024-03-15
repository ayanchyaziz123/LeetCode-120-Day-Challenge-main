from collections import defaultdict
class BreadthFirstSearch:
    def __init__(self):
        self.graph = defaultdict(int)
    def addEdge(self, src, dst):
        self.graph[src] = [dst]
        self.graph[dst] = []    