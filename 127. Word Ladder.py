class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        seq_len = 1
        HS = set(wordList)
        letters_lst = list(string.ascii_lowercase)
        def bfs():
            nonlocal seq_len
            if endWord not in HS:
                return 0

            visited = {beginWord}
            queue = deque([beginWord])

            while queue:
                for i in range(len(queue)):
                    word = queue.popleft()
                    if word == endWord:
                        return seq_len
                    for j in range(len(word)):
                        for char in letters_lst:
                            if word[j] == char:
                                continue
                            seq_word = word[:j] + char + word[j+1:]
                            if seq_word in HS and seq_word not in visited:
                                visited.add(seq_word)
                                queue.append(seq_word)
                seq_len += 1
            return 0

        return bfs()