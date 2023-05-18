# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        #O(n)time, O(1)space better than naive store and search
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False

        # # Naive method O(n)time, O(n)space
        # visited = []
        # while head:
        #     if head.next in visited:
        #         return True
        #     visited.append(head)
        #     head = head.next
        # return False