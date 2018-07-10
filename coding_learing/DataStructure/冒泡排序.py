# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 10:14:10 2018

@author: vict
"""

lis_data = [2,3,4,5,6,3,4,8,9,11,1]
lis_data = [1,2,3,4,5,6,7]
lis_len =len(lis_data)
max_unit = lis_data[0]
for i in range(lis_len - 1):
    count = 0;
    for j in range(lis_len - i - 1):
        if lis_data[j] > lis_data[j+1]:
            lis_data[j],lis_data[j+1] = lis_data[j+1],lis_data[j]
            count += 1;    #优化了[1,2,3,4,5,6,7]  这种情况
    if 0 == count:
        break
print lis_data