
def moving_to_one_side(arr):

    read_stream = len(arr) - 1
    write_stream = len(arr) - 1

    while(read_stream >= 0):

        if(arr[read_stream] != 0):
            
            arr[write_stream] = arr[read_stream]
            
            write_stream -= 1

        read_stream -= 1

    while(write_stream >= 0):

        arr[write_stream] = 0
        
        write_stream -= 1

    return arr


print(moving_to_one_side([12, 13, 8, 4, 0, 2, 0, 1, 6, 0, 7]))