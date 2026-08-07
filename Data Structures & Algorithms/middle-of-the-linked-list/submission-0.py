# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # fast pointer and slow pointer
        # 判断条件：快指针指向有效值，并且还能往下跳；
        # 如果快指针到达终点，那慢指针位置就是答案

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

