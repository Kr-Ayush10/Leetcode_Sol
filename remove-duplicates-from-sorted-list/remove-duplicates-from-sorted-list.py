class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        arr = []
        if not head:
            return None
        while head != None:
            arr.append(head.val)
            head = head.next
            
        li = []
        for i in arr:
            if i not in li:
                li.append(i)
                
        node = ListNode(li[0])
        head = node
        
        for i in range(1,len(li)):
            node.next = ListNode(li[i])
            node = node.next
            
        return head