# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeTwoSortedLists(self, list1, list2):
        
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoSortedLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoSortedLists(list1, list2.next)
            return list2


    def partitionAndMerge(self, start, end, lists):
        if start>end :
            return
        if start==end:
            return lists[start]

        mid = start + (end-start)//2

        l1 = self.partitionAndMerge(start, mid, lists)
        l2 = self.partitionAndMerge(mid+1, end, lists)

        return self.mergeTwoSortedLists(l1, l2)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        start = 0
        end = len(lists)

        result = self.partitionAndMerge(start, end-1, lists)

        return result
        