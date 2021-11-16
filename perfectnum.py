def isPerfect(num):
    numsum = 0

    for i in range(num//2 + 1):
        if num//i == 0:
            numsum += i
    if num == numsum:
        return True
    else:
        return False

num1 = int(input())
num2 = int(input())

ans_arr = []
 
for i in range(num1, num2+1):
    
    if isPerfect(i):
        ans_arr.append(i)

for i in ans_arr:
    print(i)     
