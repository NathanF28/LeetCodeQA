# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        main = ListNode()
        section = ListNode()
        part = section 
        temp = main
        curr = head
        count = 0
        while curr:
            part.next = curr # append part of the k
            part = part.next # move part pointer
            count+=1  
            if count == k:
                last = part.next   # where to start next
                part.next = None    # make sure it doesnt point anywhere since its the last of the group

                begin = self.reverse(section.next)  # get start of reversed node
                temp.next = begin   # stitch start to main
                while temp.next:
                    temp = temp.next

                section = ListNode(0)
                part = section
                count = 0
                curr = last
            else:
                curr = curr.next
        if count > 0 and count < k:
            temp.next = section.next
        return main.next 


        
    def reverse(self,node):
        prev = None
        curr = node
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        return prev

        