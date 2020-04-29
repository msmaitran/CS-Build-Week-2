class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if l1 is empty, then return l2
        if not l1:
            return l2
        # if l2 is empty, then return l1
        if not l2:
            return l1
        # if value in l1 is less than or equal to value in l2, then l1.next = merge(l1.next, l2) and return l1
        if (l1.val <= l2.val):
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        # else then l2.next = merge(l1, l2.next) and return l2
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
