# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        return self.calcDept(root, 0)
    
    def calcDept(self,root,count):
        if root is None:
            return count
        count = count+1
        left = self.calcDept(root.left, count)
        right = self.calcDept(root.right, count)
        
        return max(left,right)
        