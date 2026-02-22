# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        result1=[]
        result2=[]
        current=head
        while current :
            result1.append(current.val)
            result2.append(current.val)
            current=current.next
        return result1==result2[::-1]