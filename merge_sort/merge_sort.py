# merge sort implementation

def merge(left, right):

    merged = []
    while len(left)>0 and len(right)>0:
        if left[0]<=right[0]:
            merged.append(left[0])
            left.remove(left[0])
        else:
            merged.append(right[0])
            right.remove(right[0])

    if len(left)>0:
        merged += left

    if len(right)>0:
        merged += right

    return merged


def mergesort(A):

    if len(A) == 1:
        return A

    middle = (len(A) + 1) // 2
    left = A[:middle]
    right = A[middle:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


print(mergesort([2, 3, 1, 5, 0, -9]))
# outputs: [-9, 0, 1, 2, 3, 5]