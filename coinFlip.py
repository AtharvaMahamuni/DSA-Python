import math
num = int(input())

hNum = int(input())

flipRecord = []
totalNum = 0
workArray = []

for i in range(num):
    flipRecord.append(input())
    if flipRecord[i] == "H":
        hNum -= 1
        
        if hNum == 0:
            workArray = list(flipRecord)
        else:
            workArray = flipRecord

hCount = workArray.count("H")
tCount = workArray.count("T")
totalCount = len(workArray)

print(math.floor(hCount/totalCount*100), (100 - math.floor(hCount/totalCount*100)))