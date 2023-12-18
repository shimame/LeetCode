import ListNode

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode.ListNode(0)
        cur = ListNode.ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

nums1 = [1,2,4]
nums2 = [1,3,4]
solution = Solution()

for i in range(len(nums1)):
    if (i == len(nums1)):
        nodes1 = ListNode.ListNode(nums1[i], nums1[i+1])

print(solution.mergeTwoLists(nodes1,nodes2))