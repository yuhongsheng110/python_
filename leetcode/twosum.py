#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num1_flag = -1
        num2_flag = -1
        i = 0
        length_nums = len(nums)
        while i < length_nums:
            if (target - nums[i]) in nums:
                num1_flag = i
                num2_flag = nums.index(target - nums[i])
                if nums[num1_flag] == nums[num2_flag] and num1_flag == num2_flag:
                    num1_flag = -1
                    num2_flag = -1
                    i += 1
                    continue
                break
            i += 1
        if num1_flag != -1 and num2_flag != -1:
            ret_list = [num1_flag,num2_flag]
            ret_list.sort()
            return ret_lis
        elif num1_flag * num2_flag < 0:
	    print (num1_flag,num2_flag)
            print 'error'
        elif num1_flag == -1 and num2_flag == -1:
            return []
A = Solution()
print A.twoSum([3,3],6)
