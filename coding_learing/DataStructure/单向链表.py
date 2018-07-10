# -*- coding: utf-8 -*-
"""
Created on Fri May 11 00:24:24 2018

@author: vict
"""

class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None

class SingleLinkList(object):
    def __init__(self):
        self.head = Node(None);#空头结点
    
    def is_empty(self):
        if self.head.next != None:
            return False
        return True
    
    def length(self):
        L = 0;
        p = self.head.next
        while p:
            L += 1
            p = p.next
        return length
    
    def travel(self):
        p = self.head.next
        while p:
            print p.item
            p = p.next
    
    def add(self,item):
        p = Node(item)
        p.next = self.head.next
        self.head.next = p
        
    
    def append(self,item):
        p = self.head
        while p.next:
            p = p.next
        new_node = Node(item)
        new_node.next = None
        p.next = new_node
    
    def insert(pos,item):
        if pos < 0:
            return False
        pre = self.head
        num = 0
        while num == pos and pre:
            pre = pre.next
            num += 1
        if not pre:
            return False
        p = Node(item)
        p.next = pre.next
        pre.next = p
        return True
    
    def remove(self,item):
        p = self.head.next
        pre = self.head
        while p:
            if p.item == item:
                pre.next = p.next
                del p
            p = p.next
            pre = pre.next
    
    def search(self,item):
        p = self.head.next
        while p:
            if p.item == item:
                return p
            p = p.next
        return False
        
        
def main():
    L1 = SingleLinkList()
    L1.append('abcd')
    L1.append('abcd')
    L1.append('abcd')
    L1.append('abcd')
    L1.travel()

if __name__ == "__main__":
    main()
    