# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        to_rev = self.reverse(slow)
        curr = to_rev
        biggest = 0
        temp = head
        while curr:
            biggest = max(biggest,curr.val + temp.val)
            curr = curr.next
            temp = temp.next
        return biggest

    def reverse(self,node): 
        prev = None
        curr = node
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

        