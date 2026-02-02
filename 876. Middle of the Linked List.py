# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        steps = 0
        current = head
        
        while current is not None:
            count += 1
            current = current.next

        steps = count // 2
        current = head
        while steps > 0:
            current = current.next
            steps -= 1

        return current
    

        
