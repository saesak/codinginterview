class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        
        def merge(leftarr, rightarr):
            #helper array initialized for putting values into
            #in sorted order
            helper = []

            while len(leftarr) != 0 or len(rightarr) !=0:
                if len(leftarr) != 0 and len(rightarr) !=0:
                    if leftarr[0] <= rightarr[0]:
                        helper.append(leftarr[0])
                        leftarr.pop(0)
                    elif leftarr[0] > rightarr[0]:
                        helper.append(rightarr[0])
                        rightarr.pop(0)
                #if either one are empty, just keep adding in 
                #until nothing is left!
                elif len(leftarr) == 0 and len(rightarr) !=0:
                    helper.append(rightarr[0])
                    rightarr.pop(0)
                elif len(rightarr) == 0 and len(leftarr) !=0:
                    helper.append(leftarr[0])
                    leftarr.pop(0)
            
            return helper
        
        
        def mergesort(arr):
            print(arr)
            
            n = len(arr)
    
            if n == 1:
                return arr

            mid =  n // 2 

            leftarr = arr[:mid] #indexing in python like this returns 0 to mid-1
            rightarr = arr[mid:] #so start from mid here, end at n 

            #this progressively chunks the array down
            #until the array is all just 1 element arrays
            leftarr = mergesort(leftarr)
            rightarr = mergesort(rightarr)
            
            
            #then we merge them in order!
            return merge(leftarr, rightarr)
        
        sortedarr = mergesort(nums)
        
        return sortedarr[-k]