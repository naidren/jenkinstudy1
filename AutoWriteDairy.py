# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: AutoWriteDairy.py
# @Author: chenzw
# @Institution: Guangzhou
# @E-mail: 2648738760@qq.com
# @Site: 
# @Time: 2月 20, 2023
# ---
from DailyWork.saveReport import DailyTool

if __name__ == '__main__':
    # 这是本地记录日志任务的文件
    DailyTool().add_report(r"C:\\Users\\86166\\Desktop\\每日任务.txt")