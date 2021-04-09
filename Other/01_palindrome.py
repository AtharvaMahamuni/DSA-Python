
def rev(num):
    return str(num)[::-1]


def isItPalindrome(num):
    return str(num)[::-1] == str(num)


num = int(input())


while (1):
    num = num + int(rev(num))
    if isItPalindrome(num):
        print(num)
        break
