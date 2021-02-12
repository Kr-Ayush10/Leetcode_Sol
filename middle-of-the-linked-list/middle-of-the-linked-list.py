# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Transform graph into list in one traversal, return middle element by index
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:        
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        return nodes[int(len(nodes) / 2)]