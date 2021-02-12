# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head_num = ListNode(0)
        carry_num = 0
        curr_num = head_num
        
        while l1 or l2:
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0
            
            sum_ = l1_val + l2_val + carry_num
            
            curr_num.next = ListNode(sum_ % 10)
            curr_num = curr_num.next
            carry_num = sum_ // 10
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry_num:
            curr_num.next = ListNode(carry_num)
        
        return head_num.next