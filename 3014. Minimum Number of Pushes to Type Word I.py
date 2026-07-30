class Solution:
    def minimumPushes(self, word: str) -> int:
        pushes = 0

        if len(word) < 9:
            pushes = len(word)
        else:
            n = len(word)
            k = n//8
            pushes = 8 * (k * (k+1))//2 + n % 8 *(k + 1)

        return pushes

class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        for i in range(len(word)):
            ans += i // 8 + 1
        return ans