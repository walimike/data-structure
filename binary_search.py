
def binary_search(input_array, value):
    """Your code goes here."""
    mid_index = len(input_array) // 2
    mid_point = input_array[mid_index]
    array = input_array
    while mid_point != value:
        print(mid_point, mid_index)
        try:
            if mid_point > value:
                # print(mid_point, value, mid_index)
                array = array[:mid_index]
                mid_index = len(array) // 2
                mid_point = array[mid_index]
                if mid_point == value:
                    return input_array.index(mid_point)
            elif mid_point < value:
                array = array[mid_index+1:]
                mid_index = len(array) // 2
                mid_point = array[mid_index]
                if mid_point == value:
                    return input_array.index(mid_point)
        except:
            return -1


def recursive_binary(input_array, value):
    mid_index = len(input_array) // 2
    mid_point = input_array[mid_index]
    array = input_array
    if len(array) == 1 and array[0] != value:
        return -1
    if mid_point > value:
        array = array[:mid_index]
        mid_index = len(array) // 2
        mid_point = array[mid_index]
        if mid_point == value:
            return input_array.index(mid_point)
        return recursive_binary(array, value)
    else:
        array = array[mid_index+1:]
        mid_index = len(array) // 2
        mid_point = array[mid_index]
        if mid_point == value:
            return input_array.index(mid_point)
        return recursive_binary(array, value)

def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)

"""
Apparently Google thinks recursion is pretty cool too—if you search for "recursion" in Google's search engine, the first thing that pops up is "Did you mean: recursion". Don't get stuck in an infinite loop continuously searching "recursion"!

"""