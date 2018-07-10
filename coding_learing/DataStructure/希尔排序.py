# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 12:40:07 2018

@author: vict
"""

lis_data = [5,6,4,3,3,45,2,1,23,3,5,8,9,9,8,90,92,934,999,6767,91]
n = len(lis_data)
if n == 1:
    print 'error'
gap = n / 2
while gap > 0:
    #间隔gap进行插入排序
    for i in range(gap,n,gap):
        for j in range(i,0,-1*gap):
            if lis_data[j] < lis_data[j-gap]:
                lis_data[j],lis_data[j-gap] = lis_data[j-gap],lis_data[j]
    gap /= 2
print lis_data  
    
    