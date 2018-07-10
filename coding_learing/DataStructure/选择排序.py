# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 10:44:51 2018

@author: vict
"""

lis_data = [2,3,4,8,1,2,54,6,7,90]
for i in range(len(lis_data) - 1):
    min_unit_flag = i
    for j in range(i,len(lis_data)):
        if lis_data[min_unit_flag] > lis_data[j]:
            min_unit_flag = j
    #交换 min_unit_flag  与 i
    lis_data[min_unit_flag],lis_data[i] = lis_data[i],lis_data[min_unit_flag]

print lis_data