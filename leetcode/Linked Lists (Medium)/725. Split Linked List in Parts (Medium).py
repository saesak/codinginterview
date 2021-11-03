'''
really bad implementation --> works but beats only 7% in terms of time

better one below
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        curr = head
        
        nums = []
        
        i = 0
        
        while curr != None:
            if i > len(nums)-1:
                i = 0
            
            nums.append(curr.val)
            
            i += 1
            curr = curr.next
        
        
        n = len(nums)
        
        rem = n % k
        div = n // k
        
        res = [None for _ in range(k)]
        
        for j in range(len(res)):
            if rem > 0:
                count = -1
                rem -= 1 
            else:
                count = 0
                pointer = None
            while count < div and len(nums) > 0:
                pop_val = nums.pop(0)
                
                if res[j] == None:
                    res[j] = ListNode(pop_val)
                    pointer = res[j]
                else:
                    pointer.next = ListNode(pop_val)
                    pointer = pointer.next
                
                count += 1 
                
                    
        return res

'''
more concise implementation
taken from answers

it seems to do the same thing as mine except that

it used to use xrange instead of range, something deprecated in
python3. So i changed it to range, and the speed decreased from
better than 59% to better than 14% due to that one factor.
Huh. 

Time Complexity: O(N + k), where NN is the number of nodes in the given list. 
If kk is large, it could still require creating many new empty lists. 
Space Complexity: O(max(N, k)), the space used in writing the answer.
'''

class Solution(object):
    def splitListToParts(self, root, k):
        cur = root
        for N in range(1001):
            if not cur: break
            cur = cur.next
        width, remainder = divmod(N, k)

        ans = []
        cur = root
        for i in range(k):
            head = write = ListNode(None)
            for j in range(width + (i < remainder)):
                write.next = write = ListNode(cur.val)
                if cur: cur = cur.next
            ans.append(head.next)
        return ans