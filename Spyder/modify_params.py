# -*- coding: utf-8 -*-
"""
Created on Tue May  8 10:17:08 2018

@author: vict
"""

import time
import os
import re
def ref_config_contex():
    return \
    '''
    This is the ref parameters and the value in the list bellow
        x_Kp 1
        x_Ki 0.00
        x_Kd 0
        x_integThreshold 0.02
        x_outMax 1.0
        x_outMin 0.15
        x_slopeMax 0.10
        x_deadVol 0.05
        y_Kp 1.0
        y_Ki 0.00
        y_Kd 0
        y_integThreshold 0.10
        y_outMax 0.7
        y_outMin 0.15
        y_slopeMax 0.10
        y_deadVol 0.05
        theta_Kp 1.0
        theta_Ki 0.0
        theta_Kd 0
        theta_integThreshold 0.10
        theta_outMax 1.0
        theta_outMin 0.02
        theta_slopeMax 9999
        theta_deadVol 0.02
    '''

def modidy_config_file(fileName,parameter_str,parameter):
    '''modidy_config_file(文件路径及其对应的文件名,需要修改的文件内参数名,给定参数名对应的值)'''
    #fileNmae:路径+文件名
    def modify_param(param_group):
        return str(parameter)
    path_lis = fileName.split('/')
    Name = path_lis.pop()
    modifyed= False #修改过文件为真
    with open(fileName, "r") as f1,open('/'.join(path_lis) + '/' + "%s.2" % Name, "w") as f2:
        for line in f1:
            if parameter_str.find(' ') != -1:
               break 
            if line == '\n' or line.startswith('#') :
                continue
            #匹配边界
            pass
            #检测参数是否在文件中
            if parameter_str.lower() in line.lower() :
                modifyed = True
                #匹配此行后修改参数
                ret = re.sub(r'[\.\d]+',modify_param,line)
                print ret
                line = ret
            f2.write(line)
    if modifyed == False: #文件未修改:未找到对应变量
        #删除Name.2文件
        os.remove('/'.join(path_lis) + '/' + "%s.2" % Name)
        print 'Parameter-- ' + parameter_str +' --unknow!'
        print ref_config_contex()
        return False
    else:
        os.rename('/'.join(path_lis) + '/' + Name,'/'.join(path_lis) + '/' + "%s.bak"%(Name + time.ctime().replace(' ','_')))
        os.rename('/'.join(path_lis) + '/' +"%s.2" % Name,'/'.join(path_lis) + '/' + Name)
    print 'Modify Completed!\n\n'
    return True
    
if __name__ == '__main__':
    modidy_config_file('./params/BANMABIG.config','x_kp',123123)
#    print ref_config_contex()