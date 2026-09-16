# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        return self.calcPath(root, 0)

    def calcPath(self, root: Optional[TreeNode], sums: int) -> int:
        if root is None:
            return 0
        sums = (sums * 10) + root.val
        if root.left is None and root.right is None:
            return sums
        return self.calcPath(root.left, sums) + self.calcPath(root.right, sums)    