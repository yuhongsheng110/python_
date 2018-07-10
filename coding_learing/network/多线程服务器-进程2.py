# -*- coding: utf-8 -*-
"""
Created on Tue May  1 23:22:32 2018

@author: vict
"""

import socket
import multiprocessing
import time

def clientFun(clientSock,clientAddr):
    print 'started!!'
    try:
         while True:           
            recvData = clientSock.recv(1024)
            if len(recvData) > 0:
                print '--',clientAddr,recvData,'--'
                clientSock.send('ok')
            else:
                break
    finally:
        time.sleep(1)
        print '---'
        print 'clientClose!'
        clientSock.close()

def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind(('',8080))
    s.listen(5)
    p_lis = []
    try:
        while True:
            newClient,newAddr = s.accept()
            p = multiprocessing.Process(target=clientFun,args=(newClient,newAddr))
            p_lis.append(p)
            p.start()
            newClient.close()#多线程不可有此句！
    finally:
            print 'Server Close!'
            s.close()
            for tem in p_lis:
                tem.terminate()
    

if __name__ == '__main__':
    main()
    