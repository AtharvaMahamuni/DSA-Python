
def moveToOneSide(arr):

    readStream = writeStream = len(arr) - 1

    for i in range(len(arr)):

        if arr[readStream] != 0:
            arr[writeStream] = arr[readStream]
            writeStream -= 1
        readStream -= 1

    while writeStream >= 0:
        arr[writeStream] = 0
        writeStream -= 1

    return arr


print(moveToOneSide([1, 4, 6, 0, 1, 3, 0, 2, 5, 0, 8, 0]))
