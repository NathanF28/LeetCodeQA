"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # traverse the list sequentially
        # if theres child
         # move to the last node
         # connect it to the parent next 

        curr = head

        while curr:
            # Case 1
            if not curr.child:
                curr = curr.next
                continue
            # Case 2

            child_ptr = curr.child

            while child_ptr.next:
                child_ptr = child_ptr.next
            
            last_node = child_ptr
            last_node.next = curr.next

            if curr.next:
                curr.next.prev = last_node
                
            curr.next = curr.child
            curr.child.prev = curr

            curr.child = None

            curr = curr.next
        
        return head




            
        