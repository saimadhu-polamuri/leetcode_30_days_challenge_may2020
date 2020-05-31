__author__ = "saimadhu.polamuri"

class TreeNode:

    def __init__(self, v):
        self.val = v
        self.children = {}
        self.endhere = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode(None)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        parent = self.root
        for i, char in enumerate(word):
            if char not in parent.children:
                parent.children[char] = TreeNode(char)
            parent = parent.children[char]
            if i == len(word) - 1:
                parent.endhere = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        parent = self.root
        for char in word:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return parent.endhere


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        parent = self.root
        for char in prefix:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return True














