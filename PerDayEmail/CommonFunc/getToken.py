# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: getToken.py
# @Author: chenzw
# @Institution: Guangzhou
# @E-mail: 2648738760@qq.com
# @Site: 获取token,用于演示
# @Time: 4月 18, 2022
# ---
from selenium import webdriver
from CommonFunc.httpRequests import httpReqHelp
import ddddocr
# xinfang
# url = "http://172.168.201.207:16011/login"
# ocr = ddddocr.DdddOcr()
# driver = webdriver.Chrome()
# driver.get(url)
# driver.maximize_window()
# driver.implicitly_wait(5)
# picLink = driver.find_element_by_tag_name("img").get_attribute("src")
# pic = picLink.split(',')[-1]
# code = ocr.classification(img_base64=pic)
# print(code)
#
# class GetToken:
#     def ui_login_start(self,url):
#         self.ui_url = url
#         self.driver = webdriver.Chrome()
#         self.driver.get(self.ui_url)
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(5)
#
#     def getUiCodeVerify(self):
#         ocr = ddddocr.DdddOcr()
#         picLink = self.driver.find_element_by_tag_name("img").get_attribute("src")
#         pic = picLink.split(',')[-1]
#         code = ocr.classification(img_base64=pic)
#         return code
#
#     def Login(self,user_path,pwd_path,code_path,login_button,username,pwd):
#         self.driver.find_element_by_id(user_path).send_keys(username)
#         self.driver.find_element_by_id(pwd_path).send_keys(pwd)
#         self.driver.find_element_by_id(code_path).send_keys(self.getUiCodeVerify())
#         self.driver.find_element_by_class_name(login_button).click()
#
#
#     def getToken(self,code_url="http://172.168.201.207:16011/keyPersonnelInformation/auth/getVerifyCode",interface_url="http://172.168.201.207:16011/keyPersonnelInformation/auth/login"):
#         req_help = httpReqHelp()
#         # 获取验证码并识别
#         code_res =req_help.http_request(url=code_url,method="GET")
#         # 获取cookie，后面的登录接口要用到
#         code = ddddocr.DdddOcr().classification(img_base64=code_res.json()["data"])
#         cookies = dict(code_res.cookies)
#         login_data = {"username":"wu2","password":"282ff1c957c4c8a6ec180d4d83986c8d"}
#         login_data["verificationCode"]=code
#         res = req_help.http_request(method="post",url=interface_url,data=login_data,cookies=cookies)
#         try:
#             return res.json()["data"]["token"]
#         except Exception as e:
#             # print("获取token失败，返回的信息是：%s"%res.json())
#             return res.text
#
#
# if __name__ == "__main__":
#     code_url = "http://172.168.201.207:16011/keyPersonnelInformation/auth/getVerifyCode"
#     login_url = r"http://172.168.201.207:16011/keyPersonnelInformation/auth/login"
#     token = httpReqHelp().getXfToken(code_url,login_url)
#     print(token)