#!/usr/bin/env python
# coding=utf-8
import pdb
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
	pdb.set_trace()
        dic = {}
        lis = []
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1 #nums1 small
        for num in nums1:
            if num in dic.keys():
                dic[num] += 1
            else:
                dic[num] = 1
	pdb.set_trace()
        for key,value in dic.items():
            if key in nums2:
		while True:
		    lis += [key]
		    if dic[key] == 1:
			del dic[key]
			break
		    else:
			dic[key] -= 1

        
        return lis
    
    
    def remove_dict(self,dic,key):
        #dic[key] 一定存在
        if dic[key] == 0:
            del dic[key]
        else:
            dic[key] -= 1



def main():
    while True:
        try:
            nums1 = [1,2,2,1]
            nums2 = [2,2]
            ret = Solution().intersect(nums1, nums2)

            print ret 
        except StopIteration:
            break

if __name__ == '__main__':
    main()
