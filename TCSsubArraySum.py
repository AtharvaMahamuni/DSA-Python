def cut(part1, part2, sumArray):
    if len(part1) == 0 and len(part2) == 0:
        return

    if part1 == part2:
        if(sum(part1) == sum(part2)):
            sumArray.append(1)
        else:
            sumArray.append(0)

    cut(part1[:len(part1)//2], part1[len(part1)//2:], sumArray)
    cut(part2[:len(part2)//2], part1[len(part2)//2:], sumArray)

num = int(input())

array = []

sumArray = [1]

for i in range(num):
    array.append(int(input()))

for i in range(len(array)//2):
    cut(array[0:len(array)//2], array[len(array)//2:], sumArray)

for i in sumArray:
    print(i, end="")