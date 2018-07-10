# -*- coding: utf-8 -*-
"""
Created on Thu May  3 19:50:13 2018

@author: vict
"""
import time
import multiprocessing
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s_len = len(s)
        front_pos = 0;
        rear_pos = s_len - 1
        front_num = 0
        rear_num = 0
        while True:
            while front_pos < s_len:
                if s[front_pos].isalnum():
                    front_num += 1
                    break
                front_pos += 1
            while rear_pos >= 0:
                if s[rear_pos].isalnum():
                    rear_num += 1
                    break
                rear_pos -= 1
            if front_pos >= rear_pos:
                break
            if s[front_pos].upper() == s[rear_pos].upper():
                front_pos += 1
                rear_pos -= 1
                continue
            else:
                return False


            
        if front_num != rear_num:
            return False
        else:
            return True
            
last_worktime = 0
last_idletime = 0
def cpu_use():  
    global last_worktime, last_idletime  
    f=open("/proc/stat","r")  
    line=""  
    while not "cpu " in line: line=f.readline()  
    f.close()  
    spl=line.split(" ")  
    worktime=int(spl[2])+int(spl[3])+int(spl[4])  
    idletime=int(spl[5])  
    dworktime=(worktime-last_worktime)  
    didletime=(idletime-last_idletime)  
    rate=float(dworktime)/(didletime+dworktime)  
    cpu_t = rate*100  
    last_worktime=worktime  
    last_idletime=idletime  
    if(last_worktime==0): return 0  
#    cpu_tip = "CPU使用率："+str(cpu_t)+"%"  
#    print(cpu_tip)  
    return cpu_t  
    
a = Solution()
print a.isPalindrome("0p")
    
    
t = 1
def busy_cpu(Q):
    global t
    while True:
        time.sleep(t)
cpu_rate = 0
def run_supervison(Q):
    while True:
        time.sleep(0.05)
        cpu_rate = cpu_use()

def control_cpu_rate(Q):
    pass
q=multiprocessing.Manager().Queue()
p = multiprocessing.Pool()
p.apply_async(busy_cpu,(q,))
p.apply_async(run_supervison,(q,))
p.apply_async(control_cpu_rate,(q,))


p.join()
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    