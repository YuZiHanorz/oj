class tNode:
    def __init__(self):
        self.isword = False
        self.children = collections.defaultdict(tNode)

class Trie:

    def __init__(self):
        self.root = tNode()

    def insert(self, word: str) -> None:
        curNode = self.root
        for char in word:
            if char not in curNode.children:
                curNode.children[char] = tNode()
            curNode = curNode.children[char]
        curNode.isword = True

    def search(self, word: str) -> bool:
        curNode = self.root
        for char in word:
            if char not in curNode.children:
                return False
            curNode = curNode.children[char]
        return curNode.isword

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        for char in prefix:
            if char not in curNode.children:
                return False
            curNode = curNode.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
