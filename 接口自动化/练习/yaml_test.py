# coding:utf-8
import pytest,os
from . import yaml_util_t1


class Test_Y:
    #查看yaml文件中某个键值对
    def te1st_1(self):
        yaml_file=os.path.join(os.path.dirname(__file__), 'get_token3.yaml')
        data = yaml_util_t1.YamlUtil().read_cases_yaml(yaml_file)
        for i in data:
            print(i["name"])

    #yaml修改键值对，再新增列表
    def test_2(self):
        yaml_file=os.path.join(os.path.dirname(__file__), 'get_token3.yaml')
        data = yaml_util_t1.YamlUtil().read_cases_yaml(yaml_file) #读取yaml文件内容
        data[1]["name"]="编辑过的name123" #修改键值对
        data.append({'name': '新请求名称'}) #新增列表
        yaml_util_t1.YamlUtil().write_extract_yaml(yaml_file, data) #将修改后的文件放到yaml里


if __name__ == '__main__':
    pytest.main()
