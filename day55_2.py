class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}

    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

class Solution:
    def replaceWords(self, dictionary, sentence):
        # Create the Trie and insert all words from the dictionary
        root = TrieNode()
        for word in dictionary:
            root.insert(word)

        # Split the sentence into words
        words = sentence.split()

        # Replace each word with the shortest matching root
        result = []
        for word in words:
            curr = root
            prefix = ""

            # Construct the prefix until a valid root is found
            for c in word:
                if c not in curr.children or curr.isEnd:
                    break
                prefix += c
                curr = curr.children[c]

            # If a valid root is found, append it to the result
            result.append(prefix if curr.isEnd else word)

        return " ".join(result)

# Example usage:
sol = Solution()
dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
result = sol.replaceWords(dictionary, sentence)
print(result)
