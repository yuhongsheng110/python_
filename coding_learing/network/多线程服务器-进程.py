# -*- coding: utf-8 -*-
"""
Created on Tue May  1 20:29:14 2018

@author: vict  

程序仍然有问题！！！--进程无法启动！
"""

import socket
import multiprocessing

def clientFun(clientSock):
    print 'started!!'
    try:
         while True:           
            recvData = clientSock.recv(1024)
            if len(recvData) > 0:
                #print '--',clientAddr,recvData,'--'
                clientSock.send('ok')
            else:
                break
    finally:
        clientSock.close()
        

def main():
    s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind(('',8081))
    s.listen(5)
    try:    
        po = multiprocessing.Pool(multiprocessing.cpu_count())
        while True:
            print '-----main-----'
            clientSock,clientAddr = s.accept()
            print 'a'
            po.apply_async(clientFun,(clientSock,clientAddr))
            #clientSock.close() #多线程不应该有此句
            print 'b'
    finally:
        print 's_close'
        s.close()
        po.close()
        po.join()


if __name__ == "__main__":
    main()
