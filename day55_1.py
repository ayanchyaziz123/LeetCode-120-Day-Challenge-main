class TrieNode:
    def __init__(self):
        # Flag to indicate if the current node marks the end of a word
        self.isEnd = False
        # Dictionary to store child nodes, where keys are characters and values are TrieNodes
        self.children = {}

    def insert(self, word):
        # Insert a word into the Trie
        root = self
        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children[ch]
        root.isEnd = True

class MagicDictionary:

    def __init__(self):
        # Initialize the MagicDictionary with a Trie root node
        self.root = TrieNode()

    def buildDict(self, dictionary):
        # Build the Trie by inserting each word from the dictionary
        for word in dictionary:
            self.root.insert(word)

    def search(self, searchWord):
        def dfs(ind, word, cnt, root):
            # DFS function to search for a word with one character difference
            if cnt > 1:
                return False  # If more than one character is different, return False
            if ind == len(word):
                return cnt == 1 and root.isEnd  # Check if it's a valid word with one character difference
            if word[ind] in root.children:
                if dfs(ind + 1, word, cnt, root.children[word[ind]]):
                    return True
            for ch in root.children:
                if ch != word[ind]:
                    if dfs(ind + 1, word, cnt + 1, root.children[ch]):
                        return True
            return False

        # Start the search using DFS from the root of the Trie
        return dfs(0, searchWord, 0, self.root)

# Example usage:
obj = MagicDictionary()
obj.buildDict(["hello", "hallo", "leetcode"])
result = obj.search("hallo")
print(result)  # Output should be True
