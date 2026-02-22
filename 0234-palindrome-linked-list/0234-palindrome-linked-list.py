# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current=head
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        while slow :
            next_val=slow.next
            slow.next=prev
            prev=slow
            slow=next_val
        while prev and current:
            if prev.val!=current.val:
                return False
            prev=prev.next
            current=current.next
        return True 