

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
