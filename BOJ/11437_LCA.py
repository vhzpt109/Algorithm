import sys

input = sys.stdin.readline


def findNode(rootNode, previousNode, targetNode, currentPath, resultPath):
    if rootNode == targetNode:
        resultPath.extend(currentPath.copy())
        return True

    if not tree[rootNode]:
        return False

    for node in tree[rootNode]:
        if node == previousNode:
            continue
        currentPath.append(node)
        if findNode(node, rootNode, targetNode, currentPath, resultPath):
            return True
        currentPath.pop()

    return False


if __name__ == "__main__":
    n = int(input())

    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        node1, node2 = map(int, input().split())
        tree[node1].append(node2)
        tree[node2].append(node1)

    m = int(input())
    for _ in range(m):
        node1, node2 = map(int, input().split())

        node1Path = []
        findNode(1, -1, node1, [1], node1Path)
        node2Path = []
        findNode(1, -1, node2, [1], node2Path)

        lcaNode = None
        for i in range(min(len(node1Path), len(node2Path))):
            if node1Path[i] == node2Path[i]:
                lcaNode = node1Path[i]
            else:
                break
        print(lcaNode)