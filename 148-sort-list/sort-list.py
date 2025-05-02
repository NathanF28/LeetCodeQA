# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge(link):
            if not link.next:
                return link
            slow = link
            fast = link 
            prev = slow
            start = link 
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None
            return mergelinkedlist(merge(start),merge(slow))
        def mergelinkedlist(first,second):
            dummy = ListNode(0)
            temp = dummy
            left = first
            right = second
            while left and right:
                if left.val < right.val:
                    temp.next = left
                    temp = left
                    left = left.next
                else:
                    temp.next = right 
                    temp = right
                    right = right.next
            if right:
                temp.next = right
            if left:
                temp.next = left
            return dummy.next
        if head:
            return merge(head)
        