from __future__ import division

raw = [0.07, 0.14, 0.07]  

def norm(input_list):
    norm_list = list()

    if isinstance(input_list, list):
        sum_list = sum(input_list)

        for value in input_list:
            tmp = value  /sum_list
            norm_list.append(tmp) 

    return norm_list

print norm(raw)
