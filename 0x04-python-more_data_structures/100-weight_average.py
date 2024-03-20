#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list) > 0:
        my_dict = dict(my_list)
        num_list = []
        for i, x in zip(list(my_dict.keys()), list(my_dict.values())):
            num_list.append(i * x)
        den_list = sum(list(my_dict.values()))
        return float(sum(num_list) / den_list)
    else:
        return 0
