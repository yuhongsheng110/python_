# -*- coding: utf-8 -*-
"""
Created on Fri May 18 23:27:45 2018

@author: vict
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #找到所有字符串中最短的字符串长度
        if strs == []:
            return ''
        if len(strs) == 1:
            return strs[0]
        
 #       s_len_min = len(strs[0])
 #       for s in strs:
 #           len_tem = len(s)
 #           if s_len_min > len_tem:
 #               s_len_min = len_tem
        
        not_same_flag = False
        i = 0
        #遍历每组第i个字符串并比对
        ch_tem = ''
        while True and not not_same_flag:
            #遍历每个字符串
            for s in strs:
                try:
                    s[i]
                except:
                    not_same_flag = True
                    break
                if self.put_same_ch(s[i]) == True:
                    continue
                else:
                    not_same_flag = True
                    break
            if not_same_flag == True:
                break
            self.clear_put_same_ch()
            i += 1
        
        return strs[0][ : i] 
        
    def put_same_ch(self,ch):
        if self.last_ch == None :
            self.last_ch = ch
            return True
        elif self.last_ch == ch:
            return True
        else:
            return False
    def clear_put_same_ch(self):
        self.last_ch = None
    
    def __init__(self):
        self.last_ch = None
        
        
a = Solution()
print a.longestCommonPrefix(["cll","cla"])