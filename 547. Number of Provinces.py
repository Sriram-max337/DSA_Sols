class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        no_of_prov = 0
        visited = set()
        def dfs(i):
            visited.add(i)
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and j not in visited:
                    dfs(j)

        for i in range(len(isConnected)):
            if i not in visited:
                no_of_prov += 1
                dfs(i)

        return no_of_prov
                    