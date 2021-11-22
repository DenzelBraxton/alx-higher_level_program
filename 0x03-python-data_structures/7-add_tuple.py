#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    new_tuple = ()

    if len_a == 0:
        tuple_1 = tuple_a + (0, 0)
    if len_b == 0:
        tuple_2 = tuple_b + (0, 0)
        
    new_tuple = tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1]
    return new_tuple
