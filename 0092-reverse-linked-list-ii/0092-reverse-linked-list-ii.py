# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        current = dummy
        
        for _ in range(left-1):
            current = current.next
            
            
        node = current.next
        
        for _ in range(left,right):
            
            temp = node.next        # the node we're going to pluck out
            node.next = temp.next   # unhook it — node now skips over temp
            temp.next = current.next  # temp points at the current front of the sublist
            current.next = temp     # current now points at temp, so temp is the new front
            
        return dummy.next
        