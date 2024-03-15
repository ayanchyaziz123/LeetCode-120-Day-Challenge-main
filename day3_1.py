# Leetcode problem: 208. Implement Trie (Prefix Tree)
# Ayan's code
class Node:
    def __init__(self) -> None:
        # Initialize an array to represent children nodes for each letter in the alphabet
        self.children = [None] * 26
        self.isEnd = False  # Flag to indicate if the current node represents the end of a word
class Trie:
    def __init__(self):
        self.root = Node()  # Initialize the root node of the trie
    def insert(self, word: str) -> None:
        """
        Insert a word into the trie.Time Complexity: O(m), where m is the length of the word.
        """
        node = self.root
        for i in range(len(word)):
            ind = ord(word[i]) - ord('a')
            if not node.children[ind]:
                node.children[ind] = Node()
            node = node.children[ind]
        node.isEnd = True
    def search(self, word: str) -> bool:
        """Search for a word in the trie.Time Complexity: O(m), where m is the length of the word."""
        node = self.root
        for i in range(len(word)):
            ind = ord(word[i]) - ord('a')
            if not node.children[ind]:
                return False
            node = node.children[ind]
        return node.isEnd
    def startsWith(self, prefix: str) -> bool:
        """Check if there is any word in the trie that starts with the given prefix.
        Time Complexity: O(m), where m is the length of the prefix.
        """
        node = self.root
        for i in range(len(prefix)):
            ind = ord(prefix[i]) - ord('a')
            if not node.children[ind]:
                return False
            node = node.children[ind]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
