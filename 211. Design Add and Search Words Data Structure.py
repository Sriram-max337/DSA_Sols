class TrieNode():
    def __init__(self):
        self.HM = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.new_node = TrieNode()

    def addWord(self, word: str) -> None:
        curr_node = self.new_node
        for char in word:
            if char not in curr_node.HM:
                curr_node.HM[char] = TrieNode()
            curr_node = curr_node.HM[char]
        curr_node.is_end = True

    def search(self, word: str) -> bool:
        curr_node = self.new_node
        def search_dfs(rem_word, node):
            if not rem_word:
                return node.is_end

            for i, ch in enumerate(rem_word):
                if ch == ".":
                    for child in node.HM.values():
                        if search_dfs(rem_word[i+1:], child):
                            return True
                    return False
                if ch not in node.HM:
                    return False
                node = node.HM[ch]
            return node.is_end
        
        for idx, char in enumerate(word):
            if char == ".":
                for child_node in curr_node.HM.values():
                    if search_dfs(word[idx+1:], child_node):
                        return True
                return False
                
            if char not in curr_node.HM:
                return False
            curr_node = curr_node.HM[char]
            
        return curr_node.is_end

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)