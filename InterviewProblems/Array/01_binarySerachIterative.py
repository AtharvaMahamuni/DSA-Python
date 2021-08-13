def binary_search(arr, val):

    low = 0
    high = len(arr) - 1


    while(low <= high):

        mid = low + (high - low)//2

        if val == arr[mid]:
            return "matched at position {}".format(mid+1)
        
        elif val < arr[mid]:
            high = mid - 1
        
        else: 
            low = mid + 1
    
    return "No match found"

def main():
    print(binary_search([12, 15, 16, 18, 25, 27, 28, 36, 39], 12))

if __name__ == "__main__":
    main()