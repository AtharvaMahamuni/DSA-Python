def maxSellProblem(arr):

    globalProfit = 0
    globalSmall = arr[0]

    for i in arr:
        if i < globalSmall:
            globalSmall = i

        if (i - globalSmall) > globalProfit:
            globalProfit = i - globalSmall

    return [globalSmall, globalProfit+globalSmall, globalProfit]


print(maxSellProblem([8, 9, 5, 6, 12, 15, 14, 11]))
