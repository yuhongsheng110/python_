# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 22:48:34 2018

@author: vict
"""

lis = [5,6,4,3,3,45,2,1,23,3,5,8,9,9,8,90,92,934,999,6767,91]

def quick_sort(lis_data,_low,_high):
    if _low >= _high:
        return lis_data
    mid_value = lis_data[_low]
    low = _low
    high = _high
    while low < high:
        while low < high and lis_data[high] >= mid_value:
            high -= 1
        lis_data[low] = lis_data[high]
        while low < high and lis_data[low] < mid_value:
            low += 1
        lis_data[high] = lis_data[low]
    lis_data[low] = mid_value
    quick_sort(lis_data,_low,low-1)
    quick_sort(lis_data,low+1,_high-1)
    return lis_data
    
print quick_sort(lis,0,len(lis_data) - 1)

