# merge sort implementation

# Time complexity, Big O ==>> O(n*logn)
# Space complexity, Big O ==>> O(n)

"""
    1st:    [5, 2, 6, 4]
    2nd:    [5, 2]; [6, 4]
    3rd:    [5], [2]; [6], [4]
    4th:    [2, 5]; [4, 6]
    5th:    [2, 4, 5, 6]
"""

def merge(left, right):
    """
    part of merge sort algorithm,
    applies merging on left and right sub-arrays
    args:   left, right -> lists
    rtype:  merged -> list (sorted)
    """
    pass


def mergesort(A):
    """
    applies merge sort to list A
    """
    # merge sort is a divide-conquer algorithm,
    # it keeps dividing list into two (same) length halves till there is one element in the sub-arrays
    # so base case here is whether len(A) is 1, and if it is, we return that sub list.
    if len(A) == 1:
        return A

    # we are here with the knowledge that len(A)>1, we need to keep dividing the list
    middle = (len(A) + 1) // 2      # +1 to ensure left sub-array will have one more element when list size is odd
                                        #   e.g.    7 => 4 + 3
    left = A[:middle]       # we extract first sub-array till the middle index (exclusively).
    right = A[middle:]       # second sub-array starting from middle index (inclusively).

    # now what we need to do is calling mergesort() function recursively till we reach the base case: len(A)==1.
    left = mergesort(left)
    right = mergesort(right)

    # once we have collected left and right sub-arrays, we merge them.
    # note that the function merge is called when all division happens, and the base cases are reached
    # then it applies sorting on each sub-array and keeps merging them into one
    """
    1st:    [5, 2, 6, 4]
    2nd:    [5, 2]; [6, 4]
    3rd:    [5], [2]; [6], [4]
        now merging is started
    1st:    [2, 5]; [4, 6]
    2nd:    [2, 4, 5, 6]
    """
    return merge(left, right)
