class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry = carry // 10
        return dummy.next

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

l1 = [2,4,3]
l2 = [5,6,4]
