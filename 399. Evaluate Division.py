class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ans = []
        graph = defaultdict(list)
        c,d = 0,0
        i = 0
        for a,b in equations:
            graph[a].append((b,values[i]))
            graph[b].append((a,1/values[i]))
            i+=1
        
        def dfs(c, d, graph):
            visited = set()
            prod = 1
            if c not in graph or d not in graph:
                return -1.0
            if c == d:
                return 1.0

            def helper(node, prod):
                if node in visited:
                    return 
                visited.add(node)
                for neighbor, weight in graph[node]:
                    if neighbor == d:
                        return prod * weight
                    ans = helper(neighbor, prod * weight)
                    if ans:
                        return ans
            res = helper(c, prod)
            if res:
                return res
            else:
                return -1.0
            
        for c,d in queries:
            ans.append(dfs(c, d, graph))
        return ans