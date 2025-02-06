#coding:utf-8
import requests
import pytest
import os
import time
from common import yaml_util

class Test_kp:
    api = 'https://api.cloud.wozp.cn/'
    kp_api = 'https://eapif.wozp.cn/'
    organization_code = 'ORG2209221ERTOBCW'
    origin = 'https://nxkp-work.cloud.wozp.cn'

    def test_login(self):
        yaml_file = os.path.join(os.path.dirname(__file__), 'get_token.yaml')
        url = Test_kp.api+'auth/user/v1/login'
        headers =  {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/88.0.4324.182 Safari/537.36',
            'referer':'https://admin-nxkp.wozp.cn' ,
            'origin':'https://admin-nxkp.wozp.cn',
        }
        data = {"account":"18258796751","appKey":"WEB","sid":64,"type":2,"authOpenId":"","authType":"",
                "publicKey":"048b71fe6c74614c48c1232ba257ee94d6e2efdbe77324cdff6f3021213ac968e9d1b5452b1aea1ce917196ba52f3778bb4d52a3e2ca782c845d8a5ce6a8c41b17",
                "password":"048d46dc19e9efb0aefe455e454458bcdebf5d380a61f1de7572430a3dda62aec7663aa697f80ba52c8692c9b92170b2b251dd220b54fa29f17848b7f5b25c0cd12542058dd789fac66f2f88c7cc3f5554446b51c84f05e0494d7560c1f1c01b852ada1fb1aa26276c0b9886"}
        res =requests.post(url=url,headers=headers,json=data)
        token =res.json()["data"]["accessToken"]
        print(token)
        yaml_util.YamlUtil().write_extract_yaml(yaml_file,{'token':token})


    def test_get_token(self):
        yaml_file = os.path.join(os.path.dirname(__file__), 'get_token.yaml')
        token=yaml_util.YamlUtil().read_extract_yaml(yaml_file)["token"]
        print(token)
        url = Test_kp.kp_api+'users/update-access-token'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/88.0.4324.182 Safari/537.36',
            'Origin':Test_kp.origin ,
            'Authorization':'Bearer '+str(token),
            'authorization-platform':token,
            'X-Organization-Code':Test_kp.organization_code,
            'X-User-Type':'8'
        }
        data = {}
        res =requests.post(url=url,headers=headers,json=data)
        print(res.text)
        # raise Exception("短语判断 不是true")  #断言判断是不是响应文案，故意制造错误

if __name__ == '__main__':
    pytest.main(['-vs','--reriuns=2'])