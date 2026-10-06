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


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        no_of_prov = 0
        visited = set()
        graph = defaultdict(list)
        n = len(isConnected)
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i!=j:
                    graph[i].append(j)

        def bfs(node):
            queue = deque([node])
            nonlocal no_of_prov
            visited.add(node)

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        for prov in range(n):
            if prov not in visited:
                no_of_prov += 1
                bfs(prov)

        return no_of_prov
                    