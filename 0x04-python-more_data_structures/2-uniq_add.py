#!/usr/bin/python3
def uniq_add(my_list=[]):
    copy_list = my_list[:]
    n_list = []
    result = 0
    for x in copy_list:
        if x not in n_list:
            result += x
            n_list.append(x)
    return result
