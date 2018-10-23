#监控模块
import requests
import urllib3
from sendmail import Email_send
import time
from reques import reques

def script(urls):
    title="监控通知-中心"+ time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    wdata = []
    wurls = []
    for url in urls:
        print('正在检测：'+ url )
        res = reques(url,0.5)
        # 未成功请求
        if int(res) == 0:
            content = '警告!'+ url +'请求失败，无法访问!\n\n'
            wurls.append(url) #加入检测队列
            print(content)
        # 成功请求
        elif res == 200:
            print(url + '\n状态码为200 工作正常')
        else:
            content = '警告！页面 '+ url +'发生故障!\n状态码为: ' + str(res) +'\n\n'
            wurls.append(url) #加入检测队列
            print(content)
        print('\n')

    print('复检开始：\n')
    print('复检队列：' + str(wurls))
    for url in wurls:
        print('正在复检：' + url)
        res = reques(url,3)
        if int(res) == 0:
            content = '警告!'+ url +'请求失败，无法访问!\n\n'
            wdata.append(content)
            print(content)
        # 成功请求
        elif res == 200:
            print(url + '\n状态码为200 工作正常')
        else:
            content = '警告！页面 '+ url +'发生故障!\n状态码为: ' + str(res) +'\n\n'
            wdata.append(content)
            print(content)
        print('\n')
    wdata = ''.join(wdata)
    #Email_send(str(wdata),title)
