# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        node = head
        # handles the empty and single populated list
        if not node:
            return node
        if not node.next:
            return node

        # 0->1->2->3
        while node:
            # save the nextNode we should be traversing too
            nextNode = node.next
            node.next = prev
            prev = node # safe the current pointer before we advance to the next node
            node = nextNode
        
        # by the end, we should be at the tail which canis set to be the new head.
        return prev

        