#Selection Sort
#Runtime -> O(n^2) average and worst case
#Memory -> O(1)

def selectionsort(arr):
    n = len(arr)
    currmin = 0
    currminindx = 0
    for i in range(0,n):
        currmin = arr[i]
        currminindx = i
        for j in range(i+1, n):
            if currmin > arr[j]:
                #could also use min then use arr.index(min) instead of looping
                currmin = arr[j]
                currminindx = j
            if j == n - 1:
                arr[i], arr[currminindx] = currmin, arr[i]
    
    return arr

'''

Selection sort is like a reversed version of bubble sort, or like selection
sort, except that it takes the minimum value of the array and put it to the leftmost end,
then take the minimum value again, puts it one position to the right of index 0, and
so on. 


'''