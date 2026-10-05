class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(graph, source, destination):
            visited = set()
            order = []

            def helper(node):
                if node == destination:
                    return True
                if node in visited:
                    return
                visited.add(node)
                order.append(node)
                for neighbor in graph[node]:
                    if helper(neighbor):
                        return True
                return False
            return helper(source)
            
        return dfs(graph, source, destination)

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set([source])
        queue = deque([source])

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        if source == destination:
            return True
            
        def bfs(graph, source, destination):
            while queue:
                node = queue.popleft()
                if node == destination:
                    return True

                for neighbor in graph[node]:
                    if neighbor == destination:
                        return True

                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            return False
        return bfs(graph, source, destination)