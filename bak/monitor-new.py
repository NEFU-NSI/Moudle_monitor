import pycurl
import os
import sys
import linecache
import time #引入事件类，用来获取系统当前时间
from sendmail import Email_send
from curl import Curl

def script(urls,type):
 #msgTo = 'xxxx@xxxx.com'
 now_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
 j=1
#  data2=[{'aa':'aa'}]
 for url_split in urls:
  print(url_split)
  url_1=url_split.split('---')
  url=url_1[-1]
  recovery_title = "监控通知----%s url:%s" % (url_1[0], url) + "在" + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())) + "已经恢复"
  down_title = "监控通知----%s url:%s" % (url_1[0], url) + "在" + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())) + "无法打开"
  #print('~~~~~~~~~~~~~~~~~~~')
  #print(url)
  #引用爬去网站的类，调用结果
  url_result = Curl(url)
  c = url_result.Curl_site()
  try:
   c.perform()
   code = str(c.getinfo(c.HTTP_CODE))
   print(code+'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
  except Exception as e:
   print('--------错误信息：--------',e)
   #indexfile.close()
   #c.close()
  code = str(c.getinfo(c.HTTP_CODE))
  # print(code+'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
  filename = '%s-%s.txt' % (url_1[0], time.strftime("%Y-%m-%d", time.localtime(time.time())))
  #判断如果在网站无法打开的情况下
  if code == '0' or code=='400' or code=='500' or code=='404':
   resolveTime = 0
   Connection_Time = 0
   Transfer_Total_Time = 0
   Total_Time = 0
   # print('为000000000000000000000000000000000000000000')
   data3 = '网站:%s\n无法打开%s' % (url_1[0], url)
   # indexfile.close()
   # c.close()
   #判断网站如果挂了就发邮件
   #stat3 = Email_send(msgTo, data3, down_title)
   resole=Email_send(data3,down_title)
   print(resole)
   print(data3 + '邮件已经发送')
  else:
   #resolveTime = str(c.getinfo(c.NAMELOOKUP_TIME) * 1000) + " ms"
   # Connection_Time=str(float(c.getinfo(c.CONNECT_TIME)*1000-c.getinfo(c.NAMELOOKUP_TIME)*1000))+" ms"
   #Connection_Time = str(c.getinfo(c.CONNECT_TIME) * 1000 - c.getinfo(c.NAMELOOKUP_TIME) * 1000) + " ms"
   # Connection_Time=round(float(Connection_Time))
   #Transfer_Total_Time = str(c.getinfo(c.TOTAL_TIME) * 1000 - c.getinfo(c.PRETRANSFER_TIME) * 1000) + " ms"
   #Total_Time = str(c.getinfo(c.TOTAL_TIME) * 1000) + " ms"
   # data2=data
   # data={'url':url,'HTTP CODE':code,'resolveTime':resolveTime,'Connection_Time':Connection_Time,'Transfer_Total_Time':Transfer_Total_Time,'Total_Time':Total_Time}
   print('网站可以正常打开')
   #f = open(filename, 'a',encoding='utf-8')
   file_exit=os.path.exists(filename)
   #print(file_exit)
   #判断这个日志文件存不存在
   if(file_exit):
    #读取文件最后一行，为了读取出来最后一次的状态值
    file = open(filename, 'r',encoding='utf-8')
    linecount = len(file.readlines())
    data = linecache.getline(filename, linecount)
    file.close
    if data == '':
     print('这是'+data+'为空的数据')
    else:
     print('其他信息%s'%(data))
     explode = data.split('----')
     #判断如果读取出来的值，最后一次是异常的情况就告警
     if explode[3]=='0\n' or explode[3]=='400\n' or explode[3]=='500' or explode[3]=='404':
      data3 = '网站:%s在%s已经恢复%s' % (url_1[0], now_time,url)
      #stat3 = Email_send(msgTo, data3, recovery_title)
      resole = Email_send(data3,recovery_title)
      print(resole)
      print(data3 + '邮件已经发送')
     else:
      print('最后一次记录为其他值：%s'%(explode[3])+'-----')
   else:
    print('文件不存在')
  data2 = '\n' + url_1[0] + '----' + url + '-----' + time.strftime("%H:%M:%S", time.localtime(time.time())) + '-------' + code
  print('data2数据写入成功：' + data2)
  file = open(filename, 'a', encoding='utf-8')
  file.write(data2)
  file.close


if __name__ == "__main__":
 type = "监控通知-测试" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
 data1=['公司门户---www.luoan.com.cn','公司平台---yun.luoan.com.cn']
 #script(data1,type)
