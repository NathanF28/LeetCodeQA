# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for liste in lists:
            head = ListNode(0)
            head.next = liste
            curr = head.next
            while curr:
                heapq.heappush(heap,curr.val)
                curr = curr.next
        start = ListNode(0)
        temp = start
        while heap:
            val = heapq.heappop(heap)
            curr = ListNode(val)
            temp.next = curr
            temp = curr
        return start.next