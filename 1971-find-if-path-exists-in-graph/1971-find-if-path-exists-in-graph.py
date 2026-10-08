class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            if node == destination:          # 1. at the target?
                return True
            visited.add(node)                # 2. mark it
            for neighbour in graph[node]:    # 3. try each unmarked neighbour
                if neighbour not in visited:
                    if dfs(neighbour):
                        return True
            return False                     # 4. nothing found from here

        return dfs(source)