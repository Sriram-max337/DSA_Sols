class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        visited = set()
        visiting = set()
        graph = defaultdict(list)
        order = []
        for a,b in prerequisites:
            graph[a].append(b)

        def cycle_check(graph):
            nonlocal order
            def dfs(node, graph):
                nonlocal order
                if node in visited:
                    return True

                if node in visiting:
                    return False
                else:
                    visiting.add(node)
                    for neighbor in graph[node]:
                        if not dfs(neighbor, graph):
                            return False

                    visiting.remove(node)
                    visited.add(node)
                    order.append(node)
                    return True

            for course in range(numCourses):
                if not dfs(course, graph):
                    return False
            else:
                return True

        if not cycle_check(graph):
            return []
        else:
            return order