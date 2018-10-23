#主程序
from monitor import script
import time

file=open('urls.txt')
data=[]
while 1:
    line =file.readline()
    print(line)
    if not line:
        break
    data.append(line[0:-1])
print(str(data) + '\n资产列表载入成功\n')
script(data)
