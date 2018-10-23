'''
设置请求头
'''
import random
from user_agents import agents

# connection 我设置了close 防止连接过大
headers = {
"User-Agent": random.choice(agents),
"Connection": 'close',
"Accept-Language": 'zh-CN,zh;q=0.8',
"Accept-Encoding": 'gzip, deflate, sdch',
"Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
"referer": 'https://www.baidu.com/'
}


