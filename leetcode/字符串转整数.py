# -*- coding: utf-8 -*-
"""
Created on Tue May 15 14:11:51 2018

@author: vict
"""
def myAtoi(str):
    if str.lstrip() == '':
        print '---3---'
        return 0
    
    if (str.lstrip()[0] == '-' or str.lstrip()[0].isdigit() or str.lstrip()[0] == '+') :
        pass
    else:
        print '---2---'
        return 0

    i = 0
    num_flag = 0
    str_len = len(str)
    flag = False
    while (str[i].isdigit() or str[i] == ' ' or str[i] == '-' or str[i] == '+'):
        if str[i] == '-' or str[i] == '+':
            flag = True
        num_flag += 1
        i += 1
        if i == str_len:
            break
        if flag == True and str[i] == ' ':
            print '---'
            return 0
    try:
        num_final =  int(str[:num_flag])
    except:
        print '---1---'
        return 0
    
    
    if num_final < -2147483648:
        return -2147483648
    elif num_final > 2147483647:
        return 2147483647
    return num_final


myAtoi('-42adf')