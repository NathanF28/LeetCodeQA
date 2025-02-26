# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odds = ListNode(0)
        odd_p = odds
        evens = ListNode(0)
        even_p = evens
        curr = head
        check = -1
        while curr:
            if check == -1:
                odd_p.next = curr
                odd_p = odd_p.next
            else:
                even_p.next = curr
                even_p = even_p.next
            curr = curr.next
            check *= -1
        even_p.next = None
        odd_p.next = evens.next
        return odds.next