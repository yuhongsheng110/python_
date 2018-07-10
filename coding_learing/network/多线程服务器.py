# -*- coding: utf-8 -*-
"""
Created on Tue May  1 19:56:10 2018

@author: vict
"""

import socket
import threading

def clientDeal(clientSock,clientAddr):
    try:
        while True:
            recvData = clientSock.recv(1024)
            if len(recvData) > 0:
                print recvData
                clientSock.send('ok!!')
            else:
                break
    finally:
        clientSock.close()
        print 'close!!'
        
def main():
    try:    
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind(('',8081))
        s.listen(5)
        while True:
            print '-------main process------'
            clientSock,clientAddr = s.accept()
            t = threading.Thread(target=clientDeal,args=(clientSock,clientAddr))
            t.start()
    finally:
        s.close()
    

if __name__ == '__main__':
    main()
    