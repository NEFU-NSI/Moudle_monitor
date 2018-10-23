#!/usr/bin/env python
# -*- encoding=utf-8 -*-
import requests

f = open('urls.txt')
data=[]
while 1:
    line =f.readline()
    print(line)
    if not line:
        break
    data.append(line[0:-2])

bad_url = []
for url in data:

    sc = 000
    try:
        print("正在尝试reques的try https://>>>")
        r=requests.get('https://' + url,verify=False,timeout=0.5)
        sc = r.status_code
    except:
        try:
            print("正在尝试reques的try http://>>>")
            r = requests.get('http://' + url, verify=False, timeout=0.5)
            sc = r.status_code
        except:
            pass
    finally:
        print(str(sc) + "-----" + url)
        if sc == 200:
            pass
        else:
            bad_url.append(str(sc) + "-----" + url)

print(bad_url)