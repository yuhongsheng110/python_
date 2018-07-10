# -*- coding: utf-8 -*-
"""
Created on Tue May  1 18:22:42 2018

@author: vict
"""

import socket


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("",8081))
s.listen(5)

while True:
    print '------main-process------'
    clientsocket,clientAddr = s.accept()
        
    
    try:
        
        while True:
            recvData = clientsocket.recv(1024)
            if len(recvData) > 0:
                print "data process:",clientAddr
                clientsocket.send('ok!!!')
            else:
                print 'client closing!'
                break
    finally:
        clientsocket.close() 
        

s.close()