# -*- coding: utf-8 -*-
"""
Created on Wed May  2 00:35:55 2018

@author: vict
"""

import socket

def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('',8081))
    s.setblocking(False)
    s.listen(5)
    sock_lis = []
    try:
        while True:
            try:
                c_sock,c_addr = s.accept()            
            except:
                pass
            else:
                c_sock.setblocking(False)
                sock_lis.append((c_sock,c_addr))
                print c_addr,'上线了！'
            
            for sock,addr in sock_lis:
                try:            
                    recvData = sock.recv(1024)
                except:  #无数据
                    pass
                else:  #数据来了
                    if len(recvData) > 0:                
                        print '已收到',addr,'数据',': ',recvData
                    else:#此客户端下线
                        sock_lis.remove((sock,addr))
                        print addr,'下线了！'
    finally:
        s.close()
    
if __name__ == '__main__':
    main()