#Insertion Sort
#Runtime -> O(n^2) average and worst case
#Memory -> O(1)

def insertionsort(arr):
    n = len(arr)
    for i in range(n):
        j = i - 1
        newi = i
        while(j > 0):
            if arr[newi] < arr[j]:
                arr[newi], arr[j] = arr[j], arr[newi]
                newi = j
            j = j - 1
    return arr

'''
kind of like bubble sort except to the left, because similar to bubble sort
it's sending least elements to the right, assuming we are sorting ascending.



'''