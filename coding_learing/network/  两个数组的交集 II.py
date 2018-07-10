# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
nums1 = [1,1,1,1,2]
nums2 = [2,1]


lis = []
dic = {}
dic2 = {}
for num in nums1:
    if num not in dic.keys():
        dic[num] = 1
    else:
        dic[num] += 1

print dic.get(1)
for num in nums2:
    if num not in dic2.keys():
        dic2[num] = 1
    else:
        dic2[num] += 1
for key,value in dic.items():
    if key in dic2.keys():
        lis += [key] * min(dic[key],dic2[key])

print lis