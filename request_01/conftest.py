#实例属性
'''class student:
    address = "oihoioh"

    def __init__(self,name,age):
        self.name = name
        self.age = age
res = student("zhangsan",34)
print(res.age)

class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
za = Employee("HH",9000)
print(za.name)

#构造函数的继承
class father(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tak(self):
        print("jhoaifoijoJ")

class son(father):
    def __init__(self, name, age, sex):
        # father.__init__(self,name,age)
        # self.sex=sex
        super(son,self).__init__(name,age)
        self.sex=sex

res1 = son("hcc",21,"男")
print(res1.tak())
print("_______________")'''

class inis:
    re = [{"name":'zhangsan'},{"age":90}]
    def sso(self):
        res = inis.re
        print(type(res))

if __name__ == '__main__':
    inis()

