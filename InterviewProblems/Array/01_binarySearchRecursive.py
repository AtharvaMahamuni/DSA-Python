
def binary_search_helper(arr, val, low, high):

    if low > high:
        return "No mathch found"

    mid = low + (high - low)//2


    if val == arr[mid]:
        return "Matched at {} position".format(mid + 1)

    elif val < arr[mid]:
        return binary_search_helper(arr, val, low, mid-1)
    
    else:
        return binary_search_helper(arr, val, mid+1, high)


def binary_search(arr, val):
    return binary_search_helper(arr, val, 0, len(arr)-1)



print(binary_search([12, 15, 16, 18, 25, 27, 28, 36, 39], 39))
