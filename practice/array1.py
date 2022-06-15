
def binarySearch(arr, key):

    low = 0
    high = len(arr) - 1

    while(high >= low):
        mid = low + (high - low) // 2

        if(arr[mid] == key):
            return mid

        elif(arr[mid] < key):
            low = mid + 1

        elif(arr[mid] > key):
            high = mid - 1

    return "No element found"


print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8], 1))
