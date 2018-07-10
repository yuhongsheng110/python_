# -*- coding: utf-8 -*-
"""
Created on Wed May  2 03:22:40 2018

@author: vict
"""

import gevent
from gevent import monkey
monkey.patch_all()

def funDeal(cli):
    try:
        while True:
            recvData = cli.recv(1024)
            if recvData:
                print recvData
            else:
                cli.close()
                print 'Closed'
                break
    finally:
        cli.close()
s = gevent.socket.socket()
s.bind(('',8898))
s.listen(5)
try:
    while True:
        newClient,newAddr = s.accept()
        print 'new!!!!:',newAddr       
        gevent.spawn(funDeal,newClient)
finally:
    s.close()    
