# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case(s) go here — comparing p and q, not just checking one
        if(p is None)and(q is None):
            return True
        elif (p is None):
            return False
        elif(q is None):
            return False
        if (p.val!=q.val):
            return False
        # recursive calls — but now each call needs a pair too
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)
        return True if left_same and right_same else False
