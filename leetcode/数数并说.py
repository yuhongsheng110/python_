# -*- coding: utf-8 -*-
"""
Created on Tue May 15 12:07:53 2018

@author: vict
"""

n = 5

def fun(up_str):
    ch_temp = up_str[0]    
    ch_coun = 0
    state = True #counting
    new_str = ''
    
    len_str = len(up_str)
    i = 0
    while i < len_str:
        if ch_temp == up_str[i]:
            state = True  #计数模式
            ch_coun += 1
        else:
            if state == True:#上次为计数模式
                new_str += str(ch_coun) + ch_temp
                ch_temp = up_str[i]
                i -= 1
                ch_coun = 0
            else:
                print '---err----'
        i += 1
    #处理末尾剩余数字
    new_str += str(ch_coun) + ch_temp
    return new_str
    
    
def get_num(n):
    next_num_str = '1'
    c_num =  1
    while c_num != n:
        next_num_str = fun(next_num_str)
        c_num += 1
    return next_num_str


def main():
    
    print get_num(5)


if __name__ == "__main__":
    main()