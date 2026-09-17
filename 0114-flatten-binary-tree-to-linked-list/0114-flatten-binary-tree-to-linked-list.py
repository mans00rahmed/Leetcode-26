# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        """Do not return anything, modify root in-place instead."""
        if root is None:
            return root

        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left  # 3
        right = root.right  # 4

        if left:
            end = left
            while end.right:
                end = end.right  # left ke end chain
            end.right = right
            root.right = left
            root.left = None
        