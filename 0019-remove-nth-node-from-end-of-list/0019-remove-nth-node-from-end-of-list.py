# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        dummy = ListNode()
        dummy.next = head
        st = dummy 
        while st:
            count += 1
            st = st.next
        count = count - n
        curr = dummy
        for i in range(count-1):
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next
