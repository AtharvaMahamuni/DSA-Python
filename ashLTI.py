input1 = int(input())
input2 = list(map(int, input().split(" ")))
input3 = int(input())
input4 = [int(x) for x in input().split()]

count = 0

for i in input4:
    for j in input2:
        if i >= j:
            count += 1


print(count)