# name="congcai"
# name2=name
# print(name,name2)
# name="chifan"
# print(name,name2)
#
# import getpass
# username=input("username:")
# password=getpass.getpass("password:")


import sys,os
from sys import argv
# script,first=argv
# print "the srcipt is called:",script
# print "the first is varible is:",first


import math
# print(dir(math))
# ret=math.sqrt(16)
# print(ret)

'''num_list = [1, 2, 3, 4, 5]
print(num_list)

i = 0
while i < len(num_list):
    if num_list[i] == 2:
        num_list.pop(i)
        i -= 1
    else:
        print(num_list[i])

    i += 1

print(num_list)'''

# num_list = [1, 2, 3, 4, 5]
# print(num_list)
'''
def sum(a,b):
    sum=a+b
    return sum

print(sum(8,9))

print("___________________________")
import json
#json转json字符串       dumps函数
data_json={"age":26,"name":"从才","id":45}
data_str=json.dumps(data_json)
#编码
str=data_str.encode('utf-8').decode('unicode_escape')
print(str)
print("------------------")

#json字符串转json
data_string='{"age":26,"name":"从才","id":45}'
data_str1=json.loads(data_string,encoding="utf-8")
print(data_str1)

print(data_str1["name"])'''

print("===============================")
#json字符串写入json文件，从json文件读取数据
json_srt2='{"id":12,"name":"李四","age":33}'
with open('data.json','a',encoding='utf-8') as f:
    f.write(json_srt2)
    f.close()

# dict1=json.loads(open('data.json',encoding='utf-8'))
# print(dict1)
# print(type(dict1))


print("+++++++++++")
#getattr(commons,inp)：判断两边内容是否一样
#hasattr（commons,inp）：判断内容是否存在，是返回true，否则false
import commons
def run():
    inp = input("输入你想访问的页面的url：").strip()
    if hasattr(commons,inp):
        result = getattr(commons,inp)
        result()
    else:
        print("404：您输入的地址不存在")

if __name__ == '__main__':
    run()
