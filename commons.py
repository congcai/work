from urllib import parse  #用于encode url中的folder参数
import requests  #用户requests.post 提交post请求
import os  #用户遍历文件目录
#import cookie  #获取用户cookie（自己创建的cookie.py文件，当前项目请求必须参数，其它项目根据情况而定）
#用于获取命令行参数
import getopt
import sys
try:
    options, args = getopt.getopt(sys.argv[1:], "hp:f:", ["folder=", "proj="])
except getopt.GetoptError:
    sys.exit()
for option, value in options:
    if option in ("-f", "--folder"):
        folder_local = format(value)
        print(format(value))
    if option in ("-p", "--proj"):
        proj = format(value)


project_id = [{'project_id':'10024'},{'project_id':'1001998'}]
project_ids = [item[key] for item in project_id for key in item]
print(project_ids)

jmeter_config = os.path.join(os.getcwd(), r'conf/config.jmx')
print(jmeter_config)
import os

print(__file__)
print(os.path.dirname(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
print(os.path.abspath(os.path.dirname(__file__)) + '/settings/')

import os


# def two_abs_join(abs1, abs2):
#     # 1. 格式化路径（将路径中的 \\ 改为 \）
#     abs2 = os.fspath(abs2)
#     # 2. 将路径文件拆分
#     abs2 = os.path.splitdrive(abs2)[1]
#     # 3. 去掉开头的 斜杠
#     abs2 = abs2.strip('\\/') or abs2
#     return os.fspath(os.path.join(abs1, abs2))
#
#
#文件路径拼接：路径+文件名
abs1 = "E:\\ftp_server\\home\\zsy"
abs2 = "123.pdf"
home = os.fspath(os.path.join(abs1, abs2))
print(home)

#格式化字符串
cookie = "fajfjiaodjf"
url = "http://cloud.cninfo.com.cn.token="+cookie+""
print(url)


