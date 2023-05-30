from collections import deque
from typing import List


class Solution:
    def bfs(self, graph, visited):
        for i in range(len(graph)):
            color_table = {}
            queue = deque([i])
            color_table[i] = True

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
        return self.bfs(graph, visited)


if __name__ == "__main__":
    obj = Solution()
    # graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    # graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    graph = [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9],
     [2, 4, 5, 6, 7, 8]]
    print(obj.isBipartite(graph))