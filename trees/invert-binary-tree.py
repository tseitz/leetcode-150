from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


if __name__ == "__main__":
    # root = [4,2,7,1,3,6,9]
    root = TreeNode(val=4, left=TreeNode(val=2, left=TreeNode(val=1, left=None, right=None), right=TreeNode(val=3, left=None, right=None)), right=TreeNode(val=7, left=TreeNode(val=6, left=None, right=None), right=TreeNode(val=9, left=None, right=None)))
    # assert Solution().invertTree(root) == [4,7,2,9,6,3,1]

    # root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    # assert Solution().invertTree(root) == [2,3,1]

