# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: getCasualDatas.py
# @Author: chenzw
# @Institution: Guangzhou
# @E-mail: 2648738760@qq.com
# @Site: prestool. 底层用到的模块：win32-setctime, soupsieve, lxml, cssutils, cssselect, cachetools, premailer, loguru, faker, beautifulsoup4, yagmail, prestool
    # tool.random_name()  # 随机姓名
    # tool.random_phone()  # 随机手机号
    # tool.random_ssn()  # 随机身份证
# @Time: 3月 16, 2022
# ---
from prestool.Tool import Tool
import random

class GetTestData:
    casual_tool = Tool()
    def get_idcard_birth_gender(self,idcard:str):
        if len(idcard)==18:
            birthday = '-'.join([idcard[6:10],idcard[10:12],idcard[12:14]])
            if int(idcard[16])%2==0:
                gender = "女"
            else:
                gender = "男"
            return birthday,gender
        else:
            raise ValueError("身份证证格式必须是18位！")

    def get_idcard_number(self,num=1):
        idcard_list = list()
        if num==1:
            return self.casual_tool.random_ssn()
        elif num>1:
            for i in range(num):
                idcard_list.append(self.casual_tool.random_ssn())
            return idcard_list
        else:
            raise IndexError("身份证个数要大于0!")

    def get_HKpassID(self):
        """
        生成随机的港澳通行证。H开头是香港，M开头是澳门
        :return:
        """
        first_letter_tuple = ("H","M")
        first_letter = random.choice(first_letter_tuple)
        return first_letter+self.casual_tool.random_number(10)

    def get_passportID(self):
        """
        随机生成护照号码。因私普通护照号码格式有:14/15+7位数,G+8位数；因公普通的是:P.+7位数；
公务的是：S.+7位数 或者 S+8位数,以D开头的是外交护照.D=diplomatic
        :return:
        """
        first_letter_tuple = ("14","15","G","P.","S.","S",'D')
        first_letter=random.choice(first_letter_tuple)
        if len(first_letter)==1:
            return first_letter+self.casual_tool.random_number(8)
        elif len(first_letter)==2:
            return first_letter+self.casual_tool.random_number(7)

if __name__ == '__main__':
    tools = GetTestData()
    # birth,sex = tools.get_i
    # dcard_birth_gender("370681194507266661")
    # print(birth,sex)
    print(tools.get_idcard_number(10))