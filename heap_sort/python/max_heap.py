# Time complexity, Big O ==>> O(n*logn)
# Space complexity, Big O ==>> O(1)

# Max heap - a heap in which any parent is greater or equal to its children
# Note: max heap implementation means sorting elements in ascending order
 
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


def heapsort(A):
    """
    applies heapsort to the given heap
    """
    global HEAP_SIZE
    for _ in range(HEAP_SIZE-1):
        A[1], A[HEAP_SIZE] = A[HEAP_SIZE], A[1]
        HEAP_SIZE -= 1
        max_heapify(A, 1)

# example
A = ["TEST", 4, 6, 1, 9, 7, 2,0, -2, 8, 5]

build_max_heap(A)   # build heap
print(A)            # see the heap

heapsort(A)     # sort heap
print(A)