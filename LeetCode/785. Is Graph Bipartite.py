from collections import deque
from typing import List


class Solution:
    def bfs(self, graph, visited, start):
        color_table = {}
        queue = deque([start])
        color_table[start] = True

        while queue:
            u = queue.popleft()
            visited[u] = True
            for v in graph[u]:
                match = color_table.get(v)
                if match is None:
                    color_table[v] = not color_table[u]
                elif color_table[u] == color_table[v]:
                    return False

                if visited[v]:
                    continue

                queue.append(v)

        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [False for _ in range(len(graph))]
        start = 0
        return self.bfs(graph, visited, start)


if __name__ == "__main__":
    obj = Solution()
    # graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    print(obj.isBipartite(graph))