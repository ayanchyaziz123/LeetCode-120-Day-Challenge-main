from typing import List

class TrieNode:
    def __init__(self):
        # Initialize a Trie node with isEnd indicating if it's the end of a word
        self.isEnd = False
        # A dictionary to store child nodes
        self.children = {}

    def insert(self, word):
        # Insert a word into the Trie
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        row_size = len(board)
        col_size = len(board[0])
        visited = [[0] * col_size for _ in range(row_size)]
        root = TrieNode()

        # Insert each word into the Trie
        for word in words:
            root.insert(word)

        res = set()

        def dfs(r, c, node, word):
            # Check if current position is within the board boundaries
            # or if it's already visited or the character is not in the Trie
            if (
                r not in range(row_size)
                or c not in range(col_size)
                or visited[r][c]
                or board[r][c] not in node.children
            ):
                return

            # Mark the current position as visited
            visited[r][c] = 1

            # Move to the child node corresponding to the current character on the board
            node = node.children[board[r][c]]

            # Add the current character to the current word
            word += board[r][c]

            # If the current node marks the end of a word, add it to the result set
            if node.isEnd:
                res.add(word)

            # Explore adjacent positions in the board
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # Mark the current position as not visited for backtracking
            visited[r][c] = 0

        # Explore each position on the board
        for r in range(row_size):
            for c in range(col_size):
                dfs(r, c, root, "")

        return list(res)
