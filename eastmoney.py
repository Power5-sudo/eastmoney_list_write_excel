#_*_ coding:utf-8_*_
"""

@Time:2020/8/20 16:17
@Author:Power5Bin
@File:eastmoney.py
@IDE:PyCharm
@Email:75806318@qq.com

"""
import re
import requests
import time
import scrapy
import xlwt
from datetime import datetime
#from xlwt import *

#file = Workbook(encoding='utf-8')
#table = file.add_sheet('')
url = 'http://38.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124008126840500384924_1597911132592&pn=1&pz=50&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=&fs=b:MK0010&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f11,f62,f128,f136,f115,f152&_=1597911132730'
headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}

def site_web(url):
    try:
        res = requests.get(url,headers=headers)
        res = res.text
        print('读取网页成功')
        data_clean(res)

    except Exception:
        print('error.siteweb')
def data_clean(res):
    try:
        co = '"f12":"(.*?)".*?'  # 代码
        name = '"f14":"(.*?)".*?'  # 名称
        new = '"f2":(.*?),".*?'  # 最新价
        cm = '"f4":(.*?),".*?'  # 涨跌额 change amount
        cr = '"f3":(.*?),".*?'  # 涨跌幅 change rate
        tm = '"f5":(.*?),".*?'  # 成交量 Turnover amount
        tr = '"f6":(.*?),".*?'  # 成交额 Turnover rate
        code = re.findall(co, res)
        lname = re.findall(name, res)
        newprice = re.findall(new, res)
        change_amount = re.findall(cm, res)
        change_rate = re.findall(cr, res)
        turnover_amount = re.findall(tm, res)
        turnover_rate = re.findall(tr, res)
        listall = list(zip(code,lname,newprice,change_amount,change_rate,turnover_amount,turnover_rate))
        print(type(listall[0]))
        print(listall[0])
        print(listall[0][1])
        excel_write = xlwt.Workbook()
        excel = excel_write.add_sheet('泸深')
        head =('代码', '名称', '最新价', '涨跌额', '涨跌幅', '成交量', '成交额')
        for i in range(len(head)):
            excel.write(0, i, head[i])
        for x in range(len(listall)):
            for y in range(len(listall[0])):
                excel.write(x+1 , y, listall[x][y])
        excel_write.save('example.xls')

    except Exception:
        print('error.dataclean')



if __name__=='__main__':
    url = 'http://38.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124008126840500384924_1597911132592&pn=1&pz=50&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=&fs=b:MK0010&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f11,f62,f128,f136,f115,f152&_=1597911132730'
    site_web(url)

"""  
        print(type(code))
        code = tuple(code)
        lname = tuple(lname)
        newprice = tuple(newprice)
        change_amount = tuple(change_amount)
        change_rate = tuple(change_rate)
        turnover_amount = tuple(turnover_amount)
        turnover_rate = tuple(turnover_rate)
        print(type(code))
        print(code)
        print('数据清洗成功')
        one = zip(code,lname,newprice,change_amount,change_rate,turnover_amount,turnover_rate)
        print(one)
"""


#name = '"f14":"(.*?)".*?'  #昨收
#name = '"f14":"(.*?)".*?'  #今开
#name = '"f14":"(.*?)".*?'  #最高
#name = '"f14":"(.*?)".*?'  #最低
# + lname[x] + newprice[x] + change_amount[x] + change_rate[x] + turnover_amount[x] + turnover_rate[x]
# + ' ' + newprice[x] + ' ' + change_amount[x] + ' ' + change_rate[x] + ' ' + turnover_amount[x] + ' ' + turnover_rate[x] + '\n'
#"f14":"上证指数","
#url = ('http://38.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124008126840500384924_1597911132592&pn=1&pz=50&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=&fs=b:MK0010&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f11,f62,f128,f136,f115,f152&_=1597911132730')