#Quick Sort
#Runtime -> O(nlog(n))
#Memory -> O(log(n)) why tho?



def quicksort(arr):
    #accounts for case if array given is length 1
    #or if a partition gets to length of 1 
    if len(arr) == 1 or len(arr) == 0:
        return arr
    n = len(arr) - 1
    
    mid = int(round(n/2))

    arr[-1], arr[mid] = arr[mid], arr[-1]

    #i is left j is right
    i = 0
    j = n-1


    while(j >= i):
        while j >= i and arr[i] < arr[-1]:
            i +=1
        while j >= i and arr[j] > arr[-1]:
            j -=1
        #swap leftitem and rightitem
        if j >= i:
            arr[i], arr[j] = arr[j], arr[i]
            j -=1
            i +=1
    #swap item at leftitem index and very end of array where the pivot/middle is
    #now everything to the left is less than the pivot and everything to the right is greater
    #and the pivot is at the point where it will be in the final array
    arr[i], arr[-1] = arr[-1], arr[i]
    

    #left partition and right partition formed at the pivot/middle
    #excluding the pivot/middle
    leftp = arr[0:i]
    rightp = arr[i+1:]


    leftp = quicksort(leftp)
    rightp = quicksort(rightp)

    
    #python way of combining lists, no need to append forever!
    return leftp + [arr[i]] + rightp

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
arr = quicksort(arr)
print(arr)


'''
Stuff that I messed up on that took me literally like an hour to catch

1. I set n to be length - 1 then I put j as n - 2
BE CAREFUL ABOUT INDEXING
2. Python indexing mistake
Doing arr[0:i] actually means you're indexing from 0 to i-1, it's not i
inclusive, which is what messed up my partitioning 

bottom might be worth checking out for interviews
a bit inefficient though
https://leetcode.com/problems/sort-an-array/discuss/277127/7-line-quicksort-to-write-in-interviews-(Python)


'''