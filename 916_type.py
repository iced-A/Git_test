# -*- coding: utf-8 -*-

import requests,re
class tt:
    def login(self):
        url = "https://api-pre.cloud.wozp.cn/auth/user/v1/login"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/88.0.4324.182 Safari/537.36',
            'Origin': "https://nxkp-pre.cloud.wozp.cn"
        }
        data = {"account":"18329073711","appKey":"WEB","sid":52,"type":2,"authOpenId":"","authType":"",
                "publicKey":"04eaff8f78dcb8e02d588b1c8104e6e570ddd430f0a6a53353303b0fb0f81fb2abbbb89f0459dd583e5a862b080ae6a92cf144d5db22ae7cf9e704591a9d6afbea",
                "password":"b8d9fdd1d73097743b325496b212044683bb1b9ab2e289d3bece136522c12c43c5fda0676892d073f3a2e6dec513e9fb7ea2e1569849aff10c955f0e369600dd95a52d2ba9c66c1cfcac1e3bd0b912a1d82ba7db578ea8b0b8d6d84a563d3bf22516e3c8c5e872bc"}
        res = requests.post(url=url, headers=headers,json=data)
        return res.json()["data"]["accessToken"]

    def update_token(self):
        token =self.login()
        url = "https://reapif.wozp.cn/users/update-access-token"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/88.0.4324.182 Safari/537.36',
            'Origin': "https://nxkp-work-pre.cloud.wozp.cn",
            'X-User-Type': '8',
            'X-Organization-Code': 'ORG2212081JB993WG',
            'Authorization': 'Bearer '+token,
            'Authorization-Platform': token
        }
        data= {}
        res = requests.post(url=url, headers=headers, json=data)
        return token


    def t1(self,n):
        token=self.update_token()
        url = "https://reapif.wozp.cn/profession-categories/list?test=1&page=%s&per-page=100" %n
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/88.0.4324.182 Safari/537.36',
            'Origin': "https://nxkp-work-pre.cloud.wozp.cn",
            'X-User-Type': '8',
            'X-Organization-Code':'ORG2212081JB993WG',
            'Authorization':'Bearer '+token
        }
        res = requests.get(url=url, headers=headers)
        for i in range(len(res.json())):
            if str(res.json()[i]["plat_qualify_type"])=="2":
                text=re.sub(r'\U0001f602', '替换内容', res.json()[i]["qualify_info"]["workName"])
                print(text)

    def t2(self):
        for i in  range(1,3):
            print(i)
            self.t1(i)

        html_content = '''
        <html>
        <head>
            <title>My HTML Page</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This is a paragraph.</p>
        </body>
        </html>
        '''

        with open('my_page.html', 'w') as file:
            file.write(html_content)

if __name__ == '__main__':
    a=tt()
    a.t2()