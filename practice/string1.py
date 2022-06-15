def palindrome(s):

    left = 0
    right = len(s) - 1

    while right >= left:

        if(s[left] != s[right]):
            return "Not a palindrome"
        left += 1
        right -= 1

    return "It is a plindrome"


print(palindrome('asdfdsa'))
print(palindrome('asddsa'))
print(palindrome('addsa'))
