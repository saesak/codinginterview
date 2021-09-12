#Merge Sort
#Runtime -> O(nlog(n))
#Memory -> O(n)

def merge(leftarr, rightarr):
    #helper array initialized for putting values into
    #in sorted order
    helper = []

    #while either are not empty, continue to add in
    #elements
    while len(leftarr) != 0 or len(rightarr) !=0:
        if len(leftarr) != 0 and len(rightarr) !=0:
            if leftarr[0] <= rightarr[0]:
                helper.append(leftarr[0])
            if leftarr[0] > rightarr[0]:
                helper.append(rightarr[0])
        #if either one are empty, just keep adding in 
        #until nothing is left!
        if len(leftarr) == 0 and len(rightarr) !=0:
            helper.append(rightarr[0])
        if len(rightarr) == 0 and len(leftarr) !=0:
            helper.append(rightarr[0])
    
    return helper

def mergesort(arr):
    n = len(arr)
    
    if n == 1:
        return arr
    
    mid =  int(round((n/2)))

    leftarr = arr[0:mid]
    rightarr = arr[mid+1:n-1]

    #this progressively chunks the array down
    #until the array is all just 1 element arrays
    leftarr = mergesort(leftarr)
    rightarr = mergesort(rightarr)

    #then we merge them in order!
    return merge(leftarr, rightarr)

'''
recursive sorting algo, think divide and conquer!



'''