# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


'''
bad solution below
uses too much memory and takes too long

should try to get it within O(n) time and O(1) memory
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        node = 0
        
        ha = headA
        hb = headB
        
        a = []
        b = []
        
        while ha != None:
            a.append(ha)
            ha = ha.next
        
        while hb != None:
            b.append(hb)
            hb = hb.next
        
        len_a = len(a)
        len_b = len(b)
        
        for i in range(-1, -min(len_a, len_b)-1, -1):
            #print(a[i], b[i])
            if a[i] == b[i]:
                node = a[i]
            else:
                break
        
        
        if node == 0:
            return None
        else:
            return node
'''
other solutions

https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/785/discuss/1494505/Succint-python-solution-by-comparing-the-hashes-of-nodes
this one uses hashes and a set, takes O(n) time but O(n) space

https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/785/discuss/1491570/Commented-for-Easy-Understanding-Most-Optimized-beats-90-oror-Python
this one iterates for length then equalizes length, and equalizes, takes like O(2n) ish time, which reduces to O(n) time and O(1) space
'''