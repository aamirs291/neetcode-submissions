# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head

        #lets divide the LL into two parts and reverse the second part

        #divide the LL
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        slow.next = None

        #reverse the second half
        prev = None
        while curr:
            curr_nxt = curr.next
            curr.next = prev
            prev = curr
            curr = curr_nxt
        
        first_head = head
        second_head = prev

        while first_head and second_head:
            first_head_nxt = first_head.next
            second_head_nxt = second_head.next

            first_head.next = second_head
            second_head.next = first_head_nxt

            first_head = first_head_nxt
            second_head = second_head_nxt
        
        # print(head)
        # return head



        