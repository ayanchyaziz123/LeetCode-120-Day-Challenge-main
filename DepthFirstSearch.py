from collections import defaultdict
class DepthFirstSearch:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
        self.visited = []
    def addEdge(self, src, dst):
        self.graph[src].append(dst)
        self.graph[dst].append(src)
    def dfs(self, src):
        print(src)
        if src not in self.visited:
            self.visited.append(src)
            for cur in self.graph[src]:
                self.dfs(cur)       

dfs = DepthFirstSearch()
dfs.addEdge(0, 1)
dfs.addEdge(1, 2)
dfs.addEdge(1, 3)
dfs.addEdge(2, 4)
dfs.addEdge(3, 4)
dfs.dfs(3)        