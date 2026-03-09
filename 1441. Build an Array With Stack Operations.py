class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        out = []

        for i in range(1,n+1):
            if stack == target:
                return out

            stack.append(i)
            out.append("Push")

            if i not in target:
                stack.pop()
                out.append("Pop")

        return out