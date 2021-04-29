
def areRotation(str1, str2):

    str1 += str1

    for i in range(len(str2)):

        if str2 == str1[i:len(str2)+i]:
            return True

    return False


print(areRotation("ABACD", "CDABA"))
print(areRotation("AACD", "ACDA"))
print(areRotation("AACA", "ACDA"))
