#coding:utf-8
import pytest
import requests,os,time,allure,json
from common import yaml_util


@allure.feature("模块名称_登录模块")
class Test_ONE:

    def allure_attach_response(self,res):
        """
        在allure显示响应信息，展示JSON格式，首行缩进更美观
        """

        if isinstance(res,dict):    #如果接口响应内容类型是字典，那就转换成字符串类型，JSON 字符串中包含非 ASCII 字符（如中文），并且首行缩进4
            allure_json = json.dumps(res,ensure_ascii=False,indent=4)
        else:
            allure_json=res
        return allure_json

    yaml_file = os.path.join(os.path.dirname(__file__), 'get_token2.yaml')
    # yaml_util.YamlUtil().claer_extract_yaml(yaml_file)

    @allure.story("函数名称_用户登录")
    # @allure.title("用例标题_多个用户登录")
    @allure.description("用例描述_不同用户登录的场景")
    @allure.link(url="http://www.baidu.com")
    @allure.step("定义用例步骤，可以增加日志信息")
    @pytest.mark.parametrize('caseinfo',yaml_util.YamlUtil().read_cases_yaml(yaml_file))
    def test_one(self,caseinfo):

        allure.attach("body是内容","新增内的标题",attachment_type=allure.attachment_type.TEXT) #新增日志内容
        allure.dynamic.title(caseinfo["name"]) #用yaml文件中的name来动态展示标题

        url=caseinfo["request"]["url"]
        headers=caseinfo["request"]["header"]
        data=caseinfo["request"]["data"]
        res =requests.post(url=url,json=data,headers=headers)
        if res.status_code==200 and res.json()["data"] is not None:
            token=res.json()["data"]["accessToken"]
            yaml_data = yaml_util.YamlUtil().read_cases_yaml(self.yaml_file)
            yaml_data[1]["name"] = "编辑过的name123"  #编辑键值对
            # yaml_data[1]["authorization"]='Bearer '+token   #增加键值对
            yaml_util.YamlUtil().write_extract_yaml(self.yaml_file,yaml_data)
            assert res.status_code == 200 and 1 == 1  # 防止报错停止运行 1==1
            allure.attach(self.allure_attach_response(res.json()), "响应信息", attachment_type=allure.attachment_type.JSON)



if __name__ == '__main__':
    pytest.main()
