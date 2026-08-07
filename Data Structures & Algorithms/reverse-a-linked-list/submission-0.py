# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 要设置一个 dummy node
        # 要先把 curr.next 储存进 temp

        pre = None # dummy node
        curr = head 
        
        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp

        return pre



        