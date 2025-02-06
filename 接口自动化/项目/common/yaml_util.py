#coding:utf-8
import os
import yaml

class YamlUtil:

    #读取文件内容
    def read_extract_yaml(self,yaml_file):
        with open(yaml_file,mode="r",encoding="utf-8") as f:
            value=yaml.load(stream=f,Loader=yaml.FullLoader)
            return value

    #写入文件内容
    def write_extract_yaml(self,yaml_file,data):
        with open(yaml_file,mode='w',encoding='utf-8') as f:
            yaml.dump(data=data,stream=f,allow_unicode=True)

    #清除文件数据
    def claer_extract_yaml(self,yaml_file):
        with open(yaml_file,mode='w',encoding='utf-8') as f:
            f.truncate()

    #读取测试用例测试数据内容
    def read_cases_yaml(self,yaml_file):
        with open(yaml_file,mode="r",encoding="utf-8") as f:
            value=yaml.load(stream=f,Loader=yaml.FullLoader)
            return value
