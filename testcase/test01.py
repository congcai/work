import pytest
# data = [['小红',18],['小明',19]]
# @pytest.mark.parametrize('project_id,version',data)
# def test_api01(project_id,version):
#     print(version)
#
import os
import os.path
#rootdir = "E:\\测量工作\\测量试题\\"
#for parent,dirnames,filenames in os.walk(rootdir):
    #res = parent
    #print(filenames)

# current_path11 = os.path.abspath(__file__)
# current_path12 = os.path.abspath(os.curdir)
# print(type(current_path11),current_path12)


#def file_name(rootdir):
# for root, dirs, files in os.walk(rootdir):
#     print(root) #当前目录路径
#     print(files) #当前路径下所有非目录子文件

#拼接：文件路径+文件名
class Test_file:
    rootdir = "E:\测量工作\测量试题"

    def test_filename(self):
        L=[]
        for root, dirs, files in os.walk(Test_file.rootdir):
            for file in files:
                if os.path.splitext(file)[1] == '.docx':
                    L.append(os.path.join(root, file))
        return L
res = Test_file()
re = res.test_filename()
print(re)



# class Test_CLanguage :
#     # 下面定义了2个类变量
#     name = "C语言中文网"
#     add = "http://c.biancheng.net"
#     # 下面定义了一个say实例方法
#     def test_say(self):
#         print(Test_CLanguage.name)
# list_0 = [x * x for x in range(5)]
# print(list_0)
#
# squares = []
# for x in range(10):
#     squares.append(x)
# print(type(squares))


        # file_object.write(filename + '\n')
        # file_object.close()

#类的继承
class test_father(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def test02(self):
        return "哈哈哈"

class test_son(test_father):
    def __init__(self,name,age,sex):
        # test_father.__init__(name,age)
        # self.sex=sex
        super(test_son,self).__init__(self.name,age,sex)
        self.sex=sex

# res1 = test_son("hcc",21,"男")
# res2 = test_son.test02()
#print(res1.name)

#面向对象
class student:
    address = "oihoioh"

    def __init__(self,name,age):
        self.name = name
        self.age = age
res = student("zhangsan",34)
#print(res.name,res.age)

if __name__ == '__main__':
    pytest.main(['-vs','test01.py'])



#挪威的森林








