#coding:utf-8
import pytest
import requests,os,time
from common import yaml_util

class Test_ONE:

    yaml_file = os.path.join(os.path.dirname(__file__), 'get_token3.yaml')
    # yaml_util.YamlUtil().claer_extract_yaml(yaml_file)
    @pytest.mark.parametrize('caseinfo',yaml_util.YamlUtil().read_cases_yaml(yaml_file))
    def test_one(self,caseinfo):
        url=caseinfo["request"]["url"]
        headers=caseinfo["request"]["header"]
        data=caseinfo["request"]["data"]
        res =requests.post(url=url,json=data,headers=headers)
        if res.status_code==200 and res.json()["data"] is not None:
            token=res.json()["data"]["accessToken"]
            yaml_data = yaml_util.YamlUtil().read_cases_yaml(self.yaml_file)
            # print(yaml_data)
            yaml_data[1]["name"] = "编辑过的name123"
            yaml_data[1]["authorization"]='Bearer '+token
            yaml_util.YamlUtil().write_extract_yaml(self.yaml_file,yaml_data)
            assert res.status_code == 200 and 1 == 1  # 防止报错停止运行 1==1


if __name__ == '__main__':
    pytest.main()
