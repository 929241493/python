# coding:utf-8
import re
import requests
# 获取网页内容
r = requests.get('http://www.njupt.edu.cn/')
data = r.text
# 利用正则查找所有连接
link_list =re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,data)
for url in link_list:
    print (url)
    
#尽管看不懂代码但是跑出来了
