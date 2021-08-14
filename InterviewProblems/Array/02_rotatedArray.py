# 4, 5, 6, 1, 2, 3

def rotated_array_helper(arr, low, high):
    
    mid = low + ((high - low)//2)

    if arr[mid+1] < arr[mid]:
        return arr[mid+1]
    
    elif arr[mid] < arr[mid-1]:
        return arr[mid]
    
    elif arr[mid] > arr[high]:
        return rotated_array_helper(arr, mid+1, high)
    
    return rotated_array_helper(arr, low, mid-1)


def rotated_array(arr):
    return rotated_array_helper(arr, 0, len(arr))

print(rotated_array([6, 5, 4, 1, 2, 3]))
print(rotated_array([12, 16, 18, 24, 3, 5, 8, 10]))