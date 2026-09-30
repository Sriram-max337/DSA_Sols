class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        visited = set()
        visiting = set()
        graph = defaultdict(list)

        for a,b in prerequisites:
            graph[a].append(b)

        def dfs(node, graph):
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
                return True

        for course_pair in prerequisites:
            if not dfs(course_pair[0], graph):
                return False
        else:
            return True