#Bubble Sort
#Runtime -> O(n^2) average and worst case
#Memory -> O(1)

def bubblesort(arr):
    n = len(arr)
    for i in range(0, n - 1):
        for j in range(0, n - 1):
            if j + 1 < n - 1:
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

'''
less efficient way to swap positions

valj = arr.pop(j)
#stuff past j shifts one position to the left
#since insert inserts before a position, we do j+1
arr.insert(j+1, valj)



'''            