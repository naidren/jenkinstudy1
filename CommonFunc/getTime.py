# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: getTime.py
# @Author: chenzw
# @Institution: Guangzhou
# @E-mail: 2648738760@qq.com
# @Site: 
# @Time: 3月 16, 2022
# ---
import time
import datetime as d
from datetime import datetime
from copy import deepcopy
import copy
class TimeHelp(object):
    @staticmethod
    def get_minute_nowtime():
        return datetime.now().strftime("%Y-%m-%d %H:%M")

    @staticmethod
    def get_second_nowtime():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_str_nowtime():
        return datetime.now().strftime("%Y%m%d_%H%M%S")

    @staticmethod
    def get_day_nowtime():
        return datetime.now().strftime("%Y-%m-%d")

    @staticmethod
    def get_eidited_nowtime(year=None,month=None,day=None):
        now_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        edit_time = copy.copy(now_time)
        if year:
            edit_time=now_time.replace(now_time[0:4], str(year))
        if month:
            edit_time = edit_time.replace(now_time[5:7], str(month))
        if day:
            edit_time = edit_time.replace(now_time[8:10], str(day))
        return edit_time

    @staticmethod
    def get_week_day():
        day_tuple = ("星期一","星期二","星期三","星期四","星期五","星期六","星期天")
        return day_tuple[datetime.today().weekday()]

if __name__ == '__main__':
    # now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    # l2 = now_time.replace(now_time[0:4], str(2022))
    # print(l2)
    print(TimeHelp.get_second_nowtime())
    # now_time.replace('%d')
    print(TimeHelp.get_week_day())