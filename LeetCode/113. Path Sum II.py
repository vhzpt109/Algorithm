from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self._path = []
        if root is None:
            return []

        self.dfs(root, 0, [root.val], targetSum)
        return self._path

    def dfs(self, node: TreeNode, currentSum, currentPath, targetSum):
        if node.left is None and node.right is None:
            if currentSum + node.val == targetSum:
                self._path.append(currentPath.copy())
                return

        if node.left:
            currentPath.append(node.left.val)
            self.dfs(node.left, node.val + currentSum, currentPath, targetSum)
            currentPath.pop()
        if node.right:
            currentPath.append(node.right.val)
            self.dfs(node.right, node.val + currentSum, currentPath, targetSum)
            currentPath.pop()