# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        # middle of linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        newHead = self.reverse(slow)

        while newHead:
            if head.val != newHead.val:
                return False
            head = head.next
            newHead = newHead.next
        return True
    
    def reverse(self, head):
        pre = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        return pre
    
