
def duplicates_in_string(s):

    read_stream = 0
    write_stream = 0

    my_set = set([])

    while(read_stream < len(s)):

        if(s[read_stream] not in my_set):

            my_set.add(s[read_stream])
            s[write_stream] = s[read_stream]
            write_stream += 1

        read_stream += 1
    
    s[write_stream] = '\0'

    return s


print(duplicates_in_string("ASDSACBASDEYD"))