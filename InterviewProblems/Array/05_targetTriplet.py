def target_triplet(arr, target):

    arrayOfTriplet = []

    for i in range(len(arr) - 2):

        left = i+1
        right = len(arr) - 1

        while(left < right):

            if(arr[i]+arr[left]+arr[right] == target):
                # print(arr[i]," ", arr[low]," ", arr[high])
                arrayOfTriplet.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1

            elif(arr[i]+arr[left]+arr[right] < target):
                left += 1
            
            elif(arr[i]+arr[left]+arr[right] > target):
                right -= 1

    return arrayOfTriplet


print(target_triplet([1,2,3,4,5,6,7,8,9,10,11,12], 15))