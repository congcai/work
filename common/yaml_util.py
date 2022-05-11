import os
import yaml
import pytest

class YamlUtil():
    #读取extract.yml文件
    def read_extract_yaml(self):
        with open(os.getcwd()+"/extract.yml",mode="r",encoding="utf-8") as f:
            value = yaml.load(stream=f,yaml=yaml.FullLoader)
            return value

    #写入extract.yml文件
    def write_extract_yaml(self,data):
        with open(os.getcwd()+"/extract.yml",mode="a",encoding="utf-8") as f:
            yaml.dump(data=data,stream=f,allow_unicode=True)

    #清楚extract.yml文件历史数据
    def clear_extract_yaml(self):
        with open(os.getcwd() + "/extract.yml", mode="w", encoding="utf-8") as f:
            f.truncate()

@pytest.mark.parametrize('name,age',[['小红',18],['小明',19]])
def test_api01(self,name,age):
    print(name,age)

if __name__ == '__main__':
    pytest.main(['-vs'])