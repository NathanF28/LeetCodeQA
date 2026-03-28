# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, head in enumerate(lists):
            if head:
                heappush(heap,(head.val, i, head))
        
        dummy = ListNode()
        curr = dummy
        while heap:
            value,index, node = heappop(heap)
            if node.next:
                heappush(heap,(node.next.val,index,node.next))
            curr.next = node
            curr = node
        return dummy.next