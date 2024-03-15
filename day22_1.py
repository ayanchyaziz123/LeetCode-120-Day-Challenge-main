from typing import List
#using trie data structure to store data
class TrieNode:
    def __init__(self):
        self.children = [None] * 256
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    #inserting in trie
    def insert(self, st):
        current = self.root
        for i in range(len(st)):
            ind = ord(st[i]) - ord('a')
            if not current.children[ind]:
                current.children[ind] = TrieNode()
            current = current.children[ind]
        current.isEnd = True
    #check if folder is already exist in trie
    def check(self, st):
        current = self.root
        for i in range(len(st)):
            ind = ord(st[i]) - ord('a')
            if current.isEnd:
                return True
            if not current.children[ind]:
                return False
            current = current.children[ind]

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        trie = Trie()
        result = []
        #iterating all the words
        for f in folder:
            # checking if the word already in trie
            if not trie.check(f + '/'):
                trie.insert(f + '/')
                result.append(f)
        return result

