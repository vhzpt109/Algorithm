from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [False for _ in range(numCourses)]
        cycle_path = [False for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            graph[prerequisite[0]].append(prerequisite[1])

        for start in range(numCourses):
            if self.check_cycle_dfs(graph, visited, cycle_path, start) is False:
                return False
        return True

    def check_cycle_dfs(self, graph, visited, cycle_path, start):
        for v in graph[start]:
            if cycle_path[v]:
                return False
            if visited[v]:
                continue
            cycle_path[v] = True
            if self.check_cycle_dfs(graph, visited, cycle_path, v) is False:
                return False
            cycle_path[v] = False
            visited[v] = True

        return True


if __name__ == "__main__":
    obj = Solution()
    numCourses = 2
    # prerequisites = [[1, 0]]
    prerequisites = [[1, 0], [0, 1]]
    # numCourses = 5
    # prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]
    print(obj.canFinish(numCourses, prerequisites))
