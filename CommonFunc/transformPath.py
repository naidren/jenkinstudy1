# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: transformPath.py
# @Author: chenzw
# @Institution: Guangzhou
# @E-mail: 2648738760@qq.com
# @Site: 
# @Time: 5月 11, 2022
# ---
import os
class PathHelper:


    def get_absolute_path(self,file_path):
        '''
        获取文件的绝对路径
        :param file_path: 从项目名称开始往下一层一层写，如PycharmProjects\\CommonFunc\\transformPath.py
        :return:
        '''
        # 获取项目名称
        project_name = file_path.split('\\')[0]
        # 获取项目名称之前的路径
        path_beforce_project_name = os.path.dirname(__file__).split(project_name)[0]
        # 拼接成绝对路径
        all_path = path_beforce_project_name + file_path
        return all_path


    def report_dirpath(self):
        return self.get_absolute_path("PycharmProjects\\intefaceItems\\petitionProject\\staticDatas\\ReportFile")

if __name__ == '__main__':
    a = PathHelper().report_dirpath()
    print(a)