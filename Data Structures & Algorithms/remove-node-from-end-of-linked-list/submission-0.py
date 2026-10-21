# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        right = head
        dummy = head
        while n>0 and right:
            right = right.next
            n-=1
        
        if not right:
            return head.next
        
        while right:
            prev = dummy
            right = right.next
            dummy = dummy.next
        
        prev.next = dummy.next

        return head