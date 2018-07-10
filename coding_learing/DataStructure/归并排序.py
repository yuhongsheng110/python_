# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 21:43:18 2018

@author: vict
"""
def merge_sort(lis_data):
    n = len(lis_data)
    if n <= 1:
        return lis_data
    mid = n / 2
    left_lis = merge_sort(lis_data[:mid])
    right_lis = merge_sort(lis_data[mid:])
    right_pointer = 0
    left_pointer = 0
    lis_temp = []
    while right_pointer < len(right_lis) and left_pointer < len(left_lis):
        if right_lis[right_pointer] < left_lis[left_pointer]:
            lis_temp.append(right_lis[right_pointer])
            right_pointer += 1
        else:
            lis_temp.append(left_lis[left_pointer])
            left_pointer += 1
    lis_temp = lis_temp + right_lis[right_pointer:] + left_lis[left_pointer:]
    print [right_lis,right_lis]
    print '\n'
    return lis_temp
lis_ori = [4,5,4,3,3,3,2,2,3,333,2,2,22212,12,89]
print lis_ori
print merge_sort(lis_ori)
