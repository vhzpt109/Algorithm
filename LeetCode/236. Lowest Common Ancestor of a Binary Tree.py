# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pNodePath = []
        self.findNode(root, p, [root.val], pNodePath)
        qNodePath = []
        self.findNode(root, q, [root.val], qNodePath)

        lcaNode = None
        for i in range(min(len(pNodePath), len(qNodePath))):
            if pNodePath[i] == qNodePath[i]:
                lcaNode = TreeNode(pNodePath[i])
        return lcaNode

    def findNode(self, node, targetNode, currentPath, resultPath):
        if node.val == targetNode.val:
            resultPath.extend(currentPath.copy())
            return True

        if node.left:
            currentPath.append(node.left.val)
            if self.findNode(node.left, targetNode, currentPath, resultPath):
                return True
            currentPath.pop()
        if node.right:
            currentPath.append(node.right.val)
            if self.findNode(node.right, targetNode, currentPath, resultPath):
                return True
            currentPath.pop()
        return False