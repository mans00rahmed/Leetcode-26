# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            temp = curr.next #(save node 2 before we lose the link)
            curr.next = prev #(reverse the link — node 1 now points to None)
            prev = curr #(advance prev to node 1)
            curr = temp #(advance curr to node 2)
            
        head = prev
        return head