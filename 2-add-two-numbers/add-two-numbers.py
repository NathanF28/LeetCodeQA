

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp  = dummy

        one = l1
        two = l2
        carry = 0
        while one or two:
            first = one.val if one else 0
            second = two.val if two else 0
            carry += first + second
            v = carry % 10
            newNode = ListNode(v)
            temp.next = newNode
            temp = temp.next 
            if carry > 9:
                carry = 1
            else:
                carry = 0
            if one:
                one = one.next
            else:
                None
            if two:
                two = two.next
            else:
                None
        if carry > 0:
            temp.next = ListNode(1)
        return dummy.next

