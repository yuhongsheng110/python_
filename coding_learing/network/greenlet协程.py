# -*- coding: utf-8 -*-
"""
Created on Wed May  2 03:03:01 2018

@author: vict
"""
import time
import greenlet
def a():
    while True:
        time.sleep(0.5)
        gr2.switch()
        print 'a'
def b():
    while True:
        time.sleep(0.5)
        gr1.switch()
        print 'b'

gr1 = greenlet.greenlet(a)
gr2 = greenlet.greenlet(b)

gr1.switch()
