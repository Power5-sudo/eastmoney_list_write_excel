#_*_ coding:utf-8_*_
"""

@Time:2020/8/21 13:39
@Author:Power5Bin
@File:zb8.py
@IDE:PyCharm
@Email:75806318@qq.com

"""
import requests
import json
import re
from urllib.request import urlopen
from pprint import pprint
#解决了Json编译问题
###
###

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

def site_web(url):       #网页提取
    url = urlopen('https://dc.qiumibao.com/shuju/public/index.php?_url=/data/index&league=%E8%8B%B1%E8%B6%85&tab=%E7%A7%AF%E5%88%86%E6%A6%9C&year=[year]&_platform=web&_env=pc')

    try:
        res = json.loads(url.read().decode('utf-8'))
        res = json.dumps(res, ensure_ascii=False)
        data_clean(res)
        print(res)
        print('读取网页成功')
    except Exception:
        print('error.site')

def data_clean(x):     #数据清洗 正则表达式
    try:
        zzname = '"球队": "(.*?)".*?'   # 球队名 正则表达式
        zzcc = '"场次": "(.*?)".*?'
        zzw = '"胜": "(.*?)".*?'
        zzp = ', "平": "(.*?)".*?'
        zzl = '"负": "(.*?)".*?'
        teamname = re.findall(zzname, x)
        teamcc = re.findall(zzcc, x)
        teamw = re.findall(zzw, x)
        teamp = re.findall(zzp, x)
        teaml = re.findall(zzl, x)
        print(teamname , teamcc ,teamw ,teamp ,teaml)
        try:
            with open('teamname.txt', 'a+') as f:  # a+ 写入方式为 追加
                for x in range(20):
                    f.write(teamname[x] + ' ')
                    f.write(teamcc[x] + ' ')
                    f.write(teamw[x] + ' ')
                    f.write(teamp[x] + ' ')
                    f.write(teaml[x] + '\n')
                    print('写入成功')
        except Exception:
            print('writeerror')
    except Exception:
        print('error.data')


    #with open('indexdata.txt','wb') as f :
     #   f.write(text)
      #  f.close()





if __name__ == '__main__':
    url = 'https://dc.qiumibao.com/shuju/public/index.php?_url=/data/index&league=%E8%8B%B1%E8%B6%85&tab=%E7%A7%AF%E5%88%86%E6%A6%9C&year=[year]&_platform=web&_env=pc'
    site_web(url)