import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline


def preorder(inorderStart, inorderEnd, postorderStart, postorderEnd):
    if (inorderStart > inorderEnd) or (postorderStart > postorderEnd):
        return

    root = postorder[postorderEnd]

    left = node_position[root] - inorderStart
    right = inorderEnd - node_position[root]

    print(root, end=" ")
    preorder(inorderStart, inorderStart + left - 1, postorderStart, postorderStart + left - 1)
    preorder(inorderEnd - right + 1, inorderEnd, postorderEnd - right, postorderEnd - 1)


if __name__ == "__main__":
    n = int(input())
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))

    node_position = [0] * (n + 1)
    for i in range(n):
        node_position[inorder[i]] = i

    preorder(0, n - 1, 0, n - 1)