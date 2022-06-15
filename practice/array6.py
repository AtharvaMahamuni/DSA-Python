def targetSum(arr, sum):

    for i in range(len(arr) - 2):

        left = i + 1
        right = len(arr) - 1

        while(right > left):

            if((arr[i] + arr[left] + arr[right]) == sum):
                print([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1

            elif(arr[i] + arr[left] + arr[right] < sum):
                left += 1

            elif(arr[i] + arr[left] + arr[right] > sum):
                right -= 1


targetSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 12)
