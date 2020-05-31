__author__ = "saimadhu.polamuri"

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        for_odd = ListNode(0)
        for_even= ListNode(0)
        odd_head = for_odd
        even_head = for_even
        is_odd = True

        while head:
            if is_odd:
                for_odd.next = head
                for_odd = for_odd.next
            else:
                for_even.next = head
                for_even = for_even.next
            is_odd = not is_odd
            head = head.next

        for_even.next = None
        for_odd.next = even_head.next
        return odd_head.next



















