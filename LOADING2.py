import urllib
import urllib2
 
values = {"username":"1924635885","password":"promise12345"}
data = urllib.urlencode(values) 
url = "http://qzone.qq.com/"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()