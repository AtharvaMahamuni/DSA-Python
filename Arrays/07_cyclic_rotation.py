def rotate( arr, n):
    
    temp = arr[n - 1]
    
    for i in reversed(range(n)):
        arr[i] = arr[i - 1]
    
    arr[0] = temp
    
    return arr


a = list(map(int, input().split()))

print(rotate(a, len(a)))

for i in range(5,0, -1):
    print(i)