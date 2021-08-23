def longest_substring(s):
    
    global_max = 0
    start = 0
    diary = {}


    for red_end in range(len(s)):

        if s[red_end] in diary:
            start = max(start, (diary[s[red_end]]+1))

        diary[s[red_end]] = red_end

        global_max = max(global_max, (red_end - start + 1))

    '''
    #We can use the following code if we want to return the substring instead of its length

    '''

    substring = ''

    for i in s[start:start+global_max]:
        substring = substring + i

    return substring

    # return global_max


print(longest_substring("ABCDABCEF"))
print(longest_substring("ABCDABCEFZABC"))