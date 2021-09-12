#Selection Sort
#Runtime -> O(n^2) average and worst case
#Memory -> O(1)

def selectionsort(arr):
    n = len(arr)
    currmin = 0
    currminindx = 0
    for i in range(0, n-1):
        currmin = arr[i]
        currminindx = i
        for j in range(i+1, n - 1):
            if currmin > arr[j]:
                currmin = arr[j]
                currminindx = j
            if j == n - 1:
                arr[i], arr[currminindx] = currmin, arr[i]
    
    return arr

