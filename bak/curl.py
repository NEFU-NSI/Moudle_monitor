import sys
import pycurl
class Curl(object):
 def __init__(self,url):
  self.url=url
 def Curl_site(self):
  c=pycurl.Curl()
  #url="www.luoan.com.cn"
  #indexfile=open(os.path.dirname(os.path.realpath(__file__))+"/content.txt","wb")
  c.setopt(c.URL,self.url)
  c.setopt(c.VERBOSE,1)
  c.setopt(c.ENCODING,"gzip")
  #模拟火狐浏览器
  c.setopt(c.USERAGENT,"Mozilla/5.0 (Windows NT 6.1; rv:35.0) Gecko/20100101 Firefox/35.0")
  return c
