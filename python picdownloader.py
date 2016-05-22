#-*-coding:utf8-*-
import re
import requests

html = requests.get('http://www.qdaily.com/categories/17').text

pic_url = re.findall('"pic" src="(.*?)"',html,re.S)

i = 0 
for each in pic_url:
    url = 'http://www.qdaily.com' + each
    print('now downloading:' + url)
    pic = requests.get(url)
    fp = open('pic//' + str(i) + '.jpg','wb')
    fp.write(pic.content)
    fp.close()
    i += 1
