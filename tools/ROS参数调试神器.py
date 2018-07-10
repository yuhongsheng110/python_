# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 11:54:51 2018

@author: vict
"""
exit(0);
try:
    import cv2
    import numpy as np
    import os
    import time
except:
    print 'pip install opencv-python'
    print 'pip install numpy'
    exit(0);

def nothing(x):
    pass
def map_num(x,in_min,in_max,out_min,out_max):
    '''把一个数从一个范围变换到另一个范围。例如
    y = map(x, 1, 50, 50, 1);
    
    The function also handles negative numbers well, so that this example
    
    函数也可以处理负数，例如
    
    y = map(x, 1, 50, 50, -100);
    
    is also valid and works well.
    
    也有效和正确
    '''
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
#创建一个黑色图像
img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('A','image',0,255,nothing) #最小值默认为0 不可更改
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('C','image',0,255,nothing)
cv2.createTrackbar('D','image',0,255,nothing)
'''.....不仅仅可以加4个cv2.createTrackbar('D','image',0,255,nothing)   可以使劲加'''
switch = '0:OFF\n1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)
    if k == ord('q'):#按q键退出
        break
    
    r = cv2.getTrackbarPos('A','image')
    r = map_num(r,0,255,-10,10); #把r的范围从0-255 映射至-10到10   例如map_num(n,1,10,1,100)
    print 'r:',r                                                        #如果n为1则map_num()返回1，为10则返回100
    os.system('rostopic pub ' + '....' + str(r)); #eg...

    g = cv2.getTrackbarPos('B', 'image')
    b = cv2.getTrackbarPos('C', 'image')
    
    s = cv2.getTrackbarPos(switch, 'image')
    
    if s == 0:
        img[:]=0
    else:
        img[:]=[r,g,b]
        
    time.sleep(0.1);
    
cv2.destroyAllWindows()