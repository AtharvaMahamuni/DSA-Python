pattern = input()

plus = 0
house = 0

for i in range(len(pattern)):
    if i == 0 and pattern[i] == 'H':
        print("No")
        break

    elif pattern[i] == 'H':
        house += 1

    elif pattern[i] == '+':
        if house > 1:
            house -= 2
        else:
            house -= 1

    if house == 3:
        print("No")
        break

else:
    print("Yes")