def max_profit(arr):

    profit = 0
    minimum = arr[0]

    for i in range(0, len(arr)):

        if(arr[i] < minimum):
            minimum = arr[i]

        if((arr[i] - minimum) > profit):
            profit = arr[i] - minimum
        
    return profit


print(max_profit([12, 3, 4, 5, 7, 9, 10, 12, 8]))
print(max_profit([ 8, 9, 5, 6, 12, 11]))


