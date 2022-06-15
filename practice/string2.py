def removeDuplicate(myString):

    myRecord = set([])
    s = []
    s[:0] = myString

    readStream = writeStream = 0

    for i in range(len(s)):
        if(s[readStream] not in myRecord):
            myRecord.add(s[readStream])
            s[writeStream] = s[readStream]
            writeStream += 1
        readStream += 1

    return ''.join(s[:writeStream])


print(removeDuplicate('atharva'))
print(removeDuplicate('abbachabbadabba'))
