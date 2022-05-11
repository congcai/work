import pytest
import requests

class Testapi:
    name = "C语言中文网"
    add = "http://c.biancheng.net"

    # 下面定义了一个say实例方法
    def test_say(self):
        print(Testapi.name,Testapi.add)

    #基本用法
    # @pytest.mark.parametrize('args',['小红','小明'])
    # def test_api01(self,args):
    #     print(args)
    #
    # #解包
    # @pytest.mark.parametrize('name,age',[['小红',18],['小明',19]])
    # def test_api02(self,name,age):
    #     print(name,age)

    # def test_huya(self):
    #     url = "https://www.huya.com/"
    #     data = {}
    #     headers = {}
    #     res = requests.get(url=url,data=data,headers=headers)
    #     print(res.content)

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 'weight'

    def talk(self):
        print("person is talking....")

class Chinese(Person):
    def __init__(self, name, age, language):  # 先继承，在重构
        Person.__init__(self, name, age)  # 继承父类的构造方法，也可以写成：super(Chinese,self).__init__(name,age)
        self.language = language  # 定义类的本身属性

    def walk(self):
        print('is walking...')

class American(Person):
    pass
c = Chinese('bigberg', 22, 'Chinese')
print(c.talk())

if __name__ == '__main__':
    pytest.main(['-vs','test_api.py'])

