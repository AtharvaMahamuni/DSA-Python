
numStalls = int(input())
distArray = list(map(int, input().split(" ")))

numJuice = int(input())
juiceArray = list(map(int, input().split(" ")))


totalDist = int(input())
energy = int(input())

ans = 0


for i in range(numStalls):
    if i == 0:
        if distArray[i] > energy:
            ans = -1
            break
        else:
            dist = distArray[i] - energy
            totalDist -= dist
            energy += juiceArray.pop(0)
            ans += 1

    elif distArray[i]-distArray[i-1] > energy:
        ans = -1
        break

    elif distArray[i] < energy:
        juiceArray.pop(0)

    else:
        dist = distArray[i] - energy
        totalDist -= dist
        energy += juiceArray.pop(0)
        ans += 1


print(ans)
        

