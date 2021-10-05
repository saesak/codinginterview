# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head
        odd = ListNode(0) #dummy
        o = odd
        while h != None:
            if h.next == None:
                h.next = odd.next
                break
            o.next = ListNode(h.next.val)
            h.next = h.next.next
            
            o = o.next
            if h.next == None:
                print('hi')
                h.next = odd.next
                break
            h = h.next
            
        
        return head
    
#[1,2,3,4,5,6,7,8]