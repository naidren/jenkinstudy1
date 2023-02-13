# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: keepJournals.py
# @Author: chenzw
# @Institution: Guangzhou
# @E-mail: 2648738760@qq.com
# @Site: 
# @Time: 2月 13, 2023
# ---
from CommonFunc.getTime import TimeHelp
import random,sys
def write_today_content(content_action="测试"):
    time_help = TimeHelp()
    day_time = time_help.get_day_nowtime()
    week_day = time_help.get_week_day()
    weather_lists = ["晴","阴","多云","小雨","中雨","大雨","暴雨","雾","炎热"]
    virtual_weather = weather_lists[random.randint(0,len(weather_lists)-1)]
    content_head = day_time+" "+ week_day+" "+virtual_weather
    content_title = "美好的一天从写日记开始".format(time_help.get_second_nowtime())
    content_all = content_head+"\n"+content_title+"\n"+"今天一整天都在{0}，很棒！".format(content_action)
    with open("日记{0}.txt".format(time_help.get_str_nowtime()),"w+") as f:
        f.write(content_all)

if __name__ == '__main__':
    content = sys.argv[1]
    write_today_content(content)
    # write_today_content("回归bug")