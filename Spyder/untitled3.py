# -*- coding: utf-8 -*-
"""
Created on Wed May  9 18:49:21 2018

@author: vict
"""

'''
s = '<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpge" style="display: inline;">'

import re
print re.match(r'.+?"(http.+?)".+?"(http.+?)"',s).groups()
'''
import re

urls = [
'http://www.interoem.com/messageinfo.asp?id=35',
'http://3995503.com/class/class09/news_show.asp?id=14',
'http://lib.wzmc.edu.cn/news/onews.asp?id=769',
'http://www.zy-ls.com/alfx.asp?newsid=377&id=6',
'http://www.fincm.com/newslist.asp?id=415'
]

s  ='hello world ha ha'
re.split(r' |:|\?',s)



#print urls
new_urls = []
for url in urls:
    #print re.match(r'(http.+?//.+?/)',url).group(1)
    new_urls.append(re.sub(r'(http://.+?/).*',lambda x:x.group(1),url))
print new_urls
