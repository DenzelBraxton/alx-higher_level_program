#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    average_number = 0
    division = 0
    for j in my_list:
        average_number += j[0] * j[1]
        division += j[1]
    return float(average_number / division)
