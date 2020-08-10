def linear_search(arr, target):
    # Your code here
    found = False
    pos = 0
    while pos < len(arr):
        if arr[pos] == target:
            return -1
            break
        pos += 1

    return found 

      # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    if len(arr) == 1:
        return arr[0] == target
    
    mid = len(arr) / 2
    if arr[mid] < target:
        return binary_search(arr[:mid], target) 
    elif arr[mid] > target:
        return binary_search(arr[mid+1],target)
    else:
        return True

    return -1  # not found
