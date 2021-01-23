# merge sort implementation

# Time complexity, Big O ==>> O(n*logn)
# Space complexity, Big O ==>> O(n)

""" 
    Example of how merge sort works:
    1st:    [5, 2, 6, 4]            # given list
    2nd:    [5, 2]; [6, 4]          # divide
    3rd:    [5], [2]; [6], [4]      # divide
    4th:    [2, 5]; [4, 6]          # merge
    5th:    [2, 4, 5, 6]            # merge
"""

def merge(left, right):
    """
    part of merge sort algorithm,
    applies merging on left and right sub-arrays
    args:   left, right -> lists
    rtype:  merged -> list (sorted)
    """
    # we need new list to store the result of merging left and right lists
    merged = []

    # while there is a value in both lists, we compare first elements, 
    # and add desired one into merged list, (append to the end)
    # and most importantly we remove that element from its list
    while len(left)>0 and len(right)>0:
        if left[0]<=right[0]:
            merged.append(left[0])
            left.remove(left[0])
        else:
            merged.append(right[0])
            right.remove(right[0])

    # there might be some elements remaining in left/right lists, we also append them into merged
    while len(left)>0:
        # actually in python list can be appended in one line... 
        # but following some classical styles/conventions is also good to understand
        merged.append(left[0])
        left.remove(left[0])

    while len(right)>0:
        merged.append(right[0])
        right.remove(right[0])

    # think why we started appending from left list not right in previous two loops?!

    # we have done, just return prepared list
    return merged


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
    # note that the function merge is called when all division happens, and the base case is reached
    # then it applies sorting on each sub-array and keeps merging them into one

    return merge(left, right)
