# -*- coding: utf-8 -*-

import requests,re
class tt:
    def t1(self,n):
        url = "https://reapif.wozp.cn/profession-categories/list?test=1&page=%s&per-page=100" %n
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/88.0.4324.182 Safari/537.36',
            'Origin': "https://nxkp-work-pre.cloud.wozp.cn",
            'X-User-Type': '8',
            'X-Organization-Code':'ORG2212081JB993WG',
            'Authorization':'Bearer eyJhbGciOiJIUzM4NCJ9.eyJqdGkiOiJqd3RfaWQiLCJzdWIiOiIyMjEyMDgxSVo4Wlo3SyIsImlhdCI6MTcwMDYzODg2MCwiYXVkIjoiV0VCIiwiZXhwIjoxNzAzMjMwODYwLCJzaWQiOjUyLCJ0eXBlIjoiVVNFUiIsImdyb3VwVHlwZSI6Mn0.Va1IttlCZxFSTILFVlBbTLE7_h7nCl27UlaVFg6jk_ZPa9QYp5JkeuHBcLy_qVQS'
        }
        res = requests.get(url=url, headers=headers)
        for i in range(len(res.json())):
            if str(res.json()[i]["plat_qualify_type"])=="2":
                text=re.sub(r'\U0001f602', '替换内容', res.json()[i]["qualify_info"]["workName"])
                print(text)

    def t2(self):
        for i in  range(1,107):
            print(i)
            self.t1(i)

if __name__ == '__main__':
    a=tt()
    a.t2()