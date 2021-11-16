
height = list(map(int, input().split(" ")))

web = height[0]

for i in range(1, len(height)):

    if height[i] > height[i-1]:
        web += height[i] 
    else:
        web += 1

print(web)