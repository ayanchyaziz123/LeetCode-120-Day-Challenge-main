class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0  # Change to integer instead of dictionary
        self.isEnd = False
        
    def insert(self, key, val):
        curr = self
        for c in key:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.val = val  # Update value at the end of the key
        curr.isEnd = True

class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        self.root.insert(key, val)

    def sum(self, prefix: str) -> int:
        root = self.root
        # Traverse to the node corresponding to the prefix
        for c in prefix:
            if c in root.children:
                root = root.children[c]
            else:
                return 0  # Return 0 if prefix not found
        
        # Perform DFS to compute the sum of all values under the prefix node
        return self.dfs(root)

    def dfs(self, node: TrieNode) -> int:
        # Base case: if the node is None, return 0
        if not node:
            return 0
        
        # Initialize sum with the value at the current node
        total = node.val
        
        # Traverse all children and recursively calculate sum
        for child in node.children.values():
            total += self.dfs(child)
        
        return total
