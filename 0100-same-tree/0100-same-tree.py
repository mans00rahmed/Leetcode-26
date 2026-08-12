# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case(s) go here — comparing p and q, not just checking one
        if p is None or q is None:
            return p is q
        if p.val != q.val:
            return False
        # recursive calls — but now each call needs a pair too
        return True if  self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) else False
