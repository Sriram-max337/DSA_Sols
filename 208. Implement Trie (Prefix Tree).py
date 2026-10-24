class TrieNode():
    def __init__(self):
        self.HM = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        self.curr_node = self.node
        for char in word:
            if char not in self.curr_node.HM:
                self.curr_node.HM[char] = TrieNode()
            self.curr_node = self.curr_node.HM[char]  
        self.curr_node.is_end = True

    def search(self, word: str) -> bool:
        self.curr_node = self.node                      
        for char in word:
            if char not in self.curr_node.HM:
                return False
            self.curr_node = self.curr_node.HM[char]  
        if self.curr_node.is_end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        self.curr_node = self.node                     
        for char in prefix:
            if char not in self.curr_node.HM:
                return False
            self.curr_node = self.curr_node.HM[char]  
        return True