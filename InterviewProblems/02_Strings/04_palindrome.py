
def palindrome(s):


    '''
    This is not so great way
    '''
    # reverse = ''

    # for i in reversed(range(len(s))):
    #     reverse += s[i]

    # if(s == reverse):
    #     return "YES"
    # return "NO"


    '''
    This is more optimised because of the array
    '''
    reverse = []

    for i in reversed(range(len(s))):
        reverse.append(s[i])
    
    if(s == ''.join(reverse)):
        return "YES"
    return "NO"


print(palindrome("madamimadam"))
print(palindrome("madamiamadam"))