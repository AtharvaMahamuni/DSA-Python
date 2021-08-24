
def subset(s, index, holder):
    
    if index == len(s):
        print(holder)
        return 

    subset(s, index+1, holder+s[index])
    subset(s, index+1, holder)


subset('abc', 0, "")
subset('1234', 0, "")