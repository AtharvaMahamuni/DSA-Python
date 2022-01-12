
num = int(input())

for i in range(num):

    virus = input()
    temp = virus[0]
    keep = 0

    for i in range(0, len(virus), 2):
        
        if temp != virus[i]:
            print(0)
            keep = 0
            break
        else:
            temp = virus[i]
            keep = 1
            continue
        
    if keep:
        print(1)