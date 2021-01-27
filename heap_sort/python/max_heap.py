# Time complexity, Big O ==>> O(n*logn)
# Space complexity, Big O ==>> O(1)

HEAP_SIZE = 10

def left_child(index):
    """
    returns left child's index in the list
    """
    return 2*index

def right_child(index):
    """
    returns right child's index in the list
    """
    return (2*index+1)

def parent(index):
    """
    returns index of a parent in the list
    """
    return index//2


def max_heapify(A, index):
    """
    applies (max) heapify operation to the given list starting from the index
    """
    global HEAP_SIZE
    left = left_child(index)
    right = right_child(index)

    largest = index

    if left<=HEAP_SIZE and A[index]<A[left]:
        largest = left
    
    if right<=HEAP_SIZE and A[largest]<A[right]:
        largest = right

    if largest != index:
        A[index], A[largest] = A[largest], A[index]
        max_heapify(A, largest)


def build_max_heap(A):
    """
    builds (max) heap from the given list
    """
    global HEAP_SIZE
    for index in range(HEAP_SIZE//2, 0, -1):
        max_heapify(A, index)
