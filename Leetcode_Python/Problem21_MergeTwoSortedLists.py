from linked_list import *
from ListNode import ListNode


def mergeTwoLists(list1, list2):
    head = ListNode()
    current = head
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 or list2
    return head.next


list1 = LinkedList()
print('insert 1,2,4...')
list1.insert(1)
list1.insert(2)
list1.insert(4)

list2 = LinkedList()
print('insert 1,3,4...')
list2.insert(1)
list2.insert(3)
list2.insert(4)

print(mergeTwoLists(list1,list2))