import sys

input = sys.stdin.readline


def PreorderTraversal(root):
    if root != '.':
        print(root, end='')
        PreorderTraversal(tree[root][0])
        PreorderTraversal(tree[root][1])


def InorderTraversal(root):
    if root != '.':
        InorderTraversal(tree[root][0])
        print(root, end='')
        InorderTraversal(tree[root][1])


def PostorderTraversal(root):
    if root != '.':
        PostorderTraversal(tree[root][0])
        PostorderTraversal(tree[root][1])
        print(root, end='')


if __name__ == "__main__":
    n = int(input())

    tree = {}
    for _ in range(n):
        root, left, right = map(str, input().split())
        tree[root] = [left, right]

    PreorderTraversal('A')
    print('')
    InorderTraversal('A')
    print('')
    PostorderTraversal('A')