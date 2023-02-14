# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: httpRequests.py
# @Author: chenzw
# @Institution: Guangzhou
# @E-mail: 2648738760@qq.com
# @Site: json.dumps(sq):转化为json格式,即字符串;json.loads(data)将字符串转化字典。
# @Time: 3月 14, 2022
# ---
import requests,ddddocr,time
from CommonFunc.readFIleContent import ConfHelp
from CommonFunc.transformPath import PathHelper

class httpReqHelp:
    def http_request(self,url,method,data=None,headers=None,**kwargs):
        if method.upper()=='GET':
            res = requests.get(url=url,params=data,headers=headers,**kwargs)
            return res
        elif method.upper()=='POST':
            res = requests.post(url,json=data,headers=headers,**kwargs)
            return res
        else:
            print("当前请求方法不存在：{0}".format(method))

    def get_cookies(self,url,login_data,headers=None,**kwargs):
        #返回cookies
        cks = requests.post(url=url,data=login_data,headers=headers).cookies
        return dict(cks)

    def getXfToken(self,**login_data):
        """
        获取token，结合识别验证码和cookies
        :param login_data: 登录信息：账号、密码、验证码
        :return token || errMessage:访问成功返回token，否则抛出异常信息
        """

        conf_file = PathHelper().get_absolute_path("PycharmProjects\\intefaceItems\\petitionProject\\staticDatas\\配置参数\\login.ini")
        conhelp = ConfHelp(conf_file)
        # 获取验证码url和登录接口url
        verify_code_url = conhelp.get_one_item(section="img_url",item_key="verify_code_url")
        login_url = conhelp.get_one_item(section="img_url",item_key="login_url")
        time.sleep(1)
        # 获取验证码和cookie，登录接口要传入
        code_res =self.http_request(url=verify_code_url,method="GET")
        code = ddddocr.DdddOcr().classification(img_base64=code_res.json()["data"])
        cookies = dict(code_res.cookies)

        # 从配置文件读取登录账密;
        login_data["username"] = conhelp.get_one_item(section="logindata",item_key="username")
        login_data["password"] = conhelp.get_one_item(section="logindata", item_key="password")
        login_data["verificationCode"]=code

        res = self.http_request(method="post",url=login_url,data=login_data,cookies=cookies)
        try:
            return res.json()["data"]["token"]
        except:
            if res.json()["message"]=="登录失败次数达到5次，账户已被锁定！" or res.json()["message"]=="账户已被锁定，请30分钟后重试！":
                raise ValueError("登录错误次数超过5次，请校验账密后再登录！")
            else:
                print(res.text)
                return self.getXfToken()


if __name__ == '__main__':
    conf_file = PathHelper().get_absolute_path(
        "PycharmProjects\\intefaceItems\\petitionProject\\staticDatas\\配置参数\\login.ini")
    conhelp = ConfHelp(conf_file)
    print(conhelp.get_one_item(section="img_url",item_key="verify_code_url"))
    print(conhelp.get_one_item(section="img_url",item_key="login_url"))
    print(httpReqHelp().getXfToken())
