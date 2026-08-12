# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None and t2:
            return False
        if t2 is None and t1:
            return False
        if t1.val != t2.val:
            return False
        return (
            True
            if self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)
            else False
        )
