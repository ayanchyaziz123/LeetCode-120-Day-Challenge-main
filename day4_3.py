
#Leetcode problem:-> #211. Design Add and Search Words Data Structure
#Ayan's code
class Node:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Add a word to the Trie.

        :param word: The word to be added to the Trie.
        """
        root = self.root
        for i in range(len(word)):
            ind = ord(word[i]) - ord('a')
            if root.children[ind] is None:
                root.children[ind] = Node()
            root = root.children[ind]
        root.isEnd = True

    def search(self, word: str) -> bool:
        """
        Search for a word in the Trie. Supports wildcard '.' character.

        :param word: The word to be searched in the Trie.
        :return: True if the word exists in the Trie, False otherwise.
        """
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    # If the character is '.', recursively check all children
                    for child in cur.children:
                        if child and dfs(i + 1, child):
                            return True
                    return False
                else:
                    ind = ord(c) - ord('a')
                    if cur.children[ind] is None:
                        return False
                    cur = cur.children[ind]
            return cur.isEnd

        return dfs(0, self.root)

# Time Complexity Analysis:
# - 'addWord': O(N), where N is the length of the word.
# - 'search': O(M), where M is the total number of Trie nodes (worst case).
