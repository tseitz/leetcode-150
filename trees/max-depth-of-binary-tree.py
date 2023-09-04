from types import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # recursive DFS
    def maxDFSRecDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # breadth first search
    def maxBFSDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 1
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

    # iterative depth first search
    def maxIDFSDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [[root, 1]]
        res = 1
        while stack:
            node, depth = stack.pop()
            
            if node:
                res = max(res, depth)
                stack.extend([node.left, depth + 1])
                stack.extend([node.right, depth + 1])
        return res
