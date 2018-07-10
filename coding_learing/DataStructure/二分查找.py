# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 13:09:35 2018

@author: vict
"""

lis_data = [1,2,3,4,5,6,7,8,9,11]
def recursion_search(lis,item,low,high):
    if low == high and lis[low] != item:
        return -1
    mid= (high + low) / 2
    if lis[mid] == item:
        return mid
    if lis[mid] < item:
        low = mid + 1
        return recursion_search(lis,item,low,high)
    elif lis[mid] > item:
        high = mid - 1
        return recursion_search(lis,item,low,high)
    


def search(lis,item):
    mid  = (0 + len(lis) -1) / 2
    low = 0
    high = len(lis) - 1
    while low <= high:
        if lis[mid] == item:
            return mid
        elif lis[mid] < item:
            low = mid + 1
        elif lis[mid] > item:
            high = mid - 1
        mid = (low + high) / 2
    
    return -1

print recursion_search(lis_data,0,0,len(lis_data) - 1)
print search(lis_data,0)

