#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy_list = my_list[:]
    return list(map(lambda x: replace if x == search else x, copy_list))
