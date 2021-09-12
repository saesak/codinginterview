#Merge Sort
#Runtime -> O(nlog(n))
#Memory -> O(n)

def merge(leftarr, rightarr):
    helper = []

    while len(leftarr) != 0 or len(rightarr) !=0:
        if len(leftarr) != 0 and len(rightarr) !=0:
            if leftarr[0] <= rightarr[0]:
                helper.append(leftarr[0])
            if leftarr[0] > rightarr[0]:
                helper.append(rightarr[0])
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

    leftarr = mergesort(leftarr)
    rightarr = mergesort(rightarr)

    return merge(leftarr, rightarr)