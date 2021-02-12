# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dix = {} # to store the addresses of the nodes 
        while head:
            if id(head) in dix:
                return True # if an address is already pointed by another node i.e. there is cycle
            else:
                dix[id(head)] =  1
                head = head.next
        
        return False