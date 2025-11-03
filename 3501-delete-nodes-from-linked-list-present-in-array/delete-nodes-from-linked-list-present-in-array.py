# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        deletable = set(nums)

        # Remove deletable nodes at the start
        while head and head.val in deletable:
            head = head.next

        # Traverse and remove deletable nodes
        curr = head
        while curr and curr.next:
            if curr.next.val in deletable:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head