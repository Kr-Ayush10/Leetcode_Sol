class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary=0
        while head:
            binary=(binary<<1)+head.val
            head=head.next
        return binary