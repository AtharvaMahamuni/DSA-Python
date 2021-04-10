# Function to find the sum of contiguous subarray with maximum sum.
def maxSubArraySum(arr, size):
    # Your code here

    currentSum = -10000000
    eSum = 0

    for i in arr:

        eSum = eSum + i

        if eSum < i:
            eSum = i

        if currentSum < eSum:
            currentSum = eSum

    return currentSum


arr = list(map(int, input().split()))

print(maxSubArraySum(arr, len(arr)))
