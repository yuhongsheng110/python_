# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 11:40:03 2018

@author: vict
"""

lis_data = [5,6,4,3,3,45,2,1,23,3,5,8,9,9,8,90]
n = len(lis_data)
for i in range(1,n):
    for j in range(i,0,-1):
        if lis_data[j] < lis_data[j -1]:
            lis_data[j],lis_data[j - 1] = lis_data[j - 1],lis_data[j]
print lis_data
            
        
        
        