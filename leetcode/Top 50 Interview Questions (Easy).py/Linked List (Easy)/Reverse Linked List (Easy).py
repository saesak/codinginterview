# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        init = ListNode(0)
        init.next = head
        res = ListNode(0)
        r_curr = res
        
        def recurse(curr):
            nonlocal r_curr
            
            if curr.next == None:
                return curr
            
            
            ret = recurse(curr.next)
            r_curr.next = ListNode(ret.val)
            r_curr = r_curr.next 
            
            return curr
        
        recurse(init)
        
        return res.next