#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return
    new_dic = a_dictionary.copy()
    for key in new_dic.keys():
        new_dic[key] *= 2
    return new_dic
