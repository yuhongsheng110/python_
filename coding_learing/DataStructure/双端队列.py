# -*- coding: utf-8 -*-
"""
Created on Sat May 19 08:49:23 2018

@author: vict
"""
class DoubleQueue_list(object):
    def __init__(self):
        self.items = []
        
    def add_front(self,item):
        self.items.insert(0,item)
    
    def add_rear(self,item):
        self.items.append(item)
        
    def remove_front(self):
        if len(self.items) == 0:
            return False
        return self.items.pop(0)
    
    def remove_rear(self):
        if len(self.items) == 0:
            return False
        return self.items.pop(0)
    
    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    
    def size(self):
        return len(self.items)
        
        
class DoubleQueue_dict(object):
    def __init__(self):
        self.items = {}
        self.add_rear_num = 0
        self.add_front_num = -1
    
    def add_front(self,item):
        self.items[self.add_front_num] = item
        self.add_front_num -= 1
    
    def add_rear(self,item):
        self.items[self.add_rear_num] = item
        self.add_rear_num += 1
    
    def remove_front(self):
        if self.add_front_num == -1 and self.add_rear_num == 0:
            return False
        data_temp = self.items[self.add_front_num + 1]
        del self.items[self.add_front_num + 1]
        self.add_front_num += 1
        return data_temp
        
    def remove_rear(self):
        if self.add_front_num == -1 and self.add_rear_num == 0:
            return False
        data_temp = self.items[self.add_rear_num - 1]
        del self.items[self.add_rear_num - 1]
        self.add_rear_num -= 1
        return data_temp
    
    def size(self):
        return self.add_rear_num - self.add_front_num - 1
        
Q = DoubleQueue_list()
Q.add_front(10)
print Q.size()
Q.remove_front()
print Q.size()
Q.add_rear(1)
print Q.remove_rear()
print '---------'





