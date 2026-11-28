class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        HM = {}
        def word_segment(i):
            if i == len(s):
                return True

            if i not in HM:
                HM[i] = False
                for j in range(i,len(s)):
                    if s[i:j+1] in word_set:
                        if word_segment(j+1):
                            HM[i] = True
                            break
            return HM[i]

        return word_segment(0)