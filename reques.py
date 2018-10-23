#模拟请求模块
import requests
import urllib3
from sendmail import Email_send
import time
from middlewares import headers

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def reques(url,timeout):
    # 状态码
    sc = 0
    type = 1
    # 分别尝试http和https
    try:
        print("正在尝试reques的try https://>>>")
        #r=requests.get('https://' + url,headers=headers,verify=False,timeout=3)
        r = requests.get('https://' + url,headers=headers, verify=False, timeout=timeout)
        sc = r.status_code
    except:
        try:
            print("正在尝试reques的try http://>>>")
            #r = requests.get('http://' + url, headers=headers, verify=False, timeout=3)
            r = requests.get('http://' + url,headers=headers, verify=False, timeout=timeout)
            sc = r.status_code
        except:
            pass
    finally:
        # 返回200为正常，否则就返回异常代码
        if(sc==200):
            return 200
        else:
            return str(sc)
