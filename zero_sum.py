def subArrayExists(arr, n):
    n_sum = 0
    s = set()
 
    for i in range(n):
        n_sum += arr[i]

        if n_sum == 0 or n_sum in s:
            return True
        s.add(n_sum)
 
    return False
 
num = int(input())

for i in range(num):
    
    arr = list(map(int, input().split(" ")))
    if subArrayExists(arr, len(arr)) == True:
        print("true")
    else:
        print("false")

