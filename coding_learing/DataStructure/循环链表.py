# -*- coding: utf-8 -*-
"""
Created on Fri May 11 09:17:55 2018

@author: vict
"""

class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None
class DoubleLinkList(object):
    def __init__(self):
        self.head = Node(None)
    
    def is_empty(self):
        if self.head.next == self.head:
            return True
        return False
        
    
    def length(self):
        p = self.head
        num = 0
        while p.next != self.head:
            num += 1
            p = p.next
        return num
        
    
    def travel(self):
        p = self.head
        while p.next != self.head:
            print p.item
            p = p.next
        print p.item
        return True
            
    
    def add(self,item):
        p_new = Node(item)
        p_new.next = self.head.next
        self.head.next = p_new
        return True
        
    
    def append(self,item):
        p = self.head
        while p.next != self.head:
            p = p.next
        p_new = Node(item)
        p.next = p_new
    
    def insert(self,pos,item):
        pre = self.head
        p = self.head.next
        num = 0
        while p != self.head and num != pos:
            num += 1
            p = p.next
            pre = pre.next
        p_new = Node(item)
        p_new.next = p
        pre.next = p_new
        return True
        
    
    def remove(self,item):
        pre = self.head
        p = self.head.next
        while p != self.head:
            if p.item == item:
                pre.next = p.next
                del p
            p = p.next
            pre = pre.next
        return True
    
    def search(self,item):
        p = self.head.next
        while p != self.head:
            if p.item == item:
                return p
            p= p.next
        return False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    