# quicksort implementation
# 1. partition function
# 2. quicksort function

# Time complexity, Worst-case ==>> O(n*logn)
#            Average-Expected ==>> O(n*logn)
# Space complexity, Big O ==>> O(1), in-place algorithm

def partition(A, p, r):
    """
    implementation of partition function used for quicksort
    """
    pivot = A[r]    # select pivot element
    i = p - 1
    for j in range(p, r):
        if A[j]<pivot:      # if an element is less than a pivot, exchange i and jth elements
            i+=1
            A[j], A[i] = A[i], A[j]
    A[r], A[i+1] = A[i+1], pivot        # at the end exchange pivot with i+1 th element of the list
    return i+1      # return the index where partition should be performed

def quicksort(A, p, r):
    """
    implementation of quicksort
    """
    if p<r:
        q = partition(A, p, r)      # select an index to apply partition
        quicksort(A, p, q-1)        # apply quicksort for left side
        quicksort(A, q+1, r)        # apply quicksort for right side

# Example
A = [9,7, 4, 6, 2, 5]
quicksort(A, 0, len(A)-1)
print(A)
# which prints: [2, 4, 5, 6, 7, 9]
