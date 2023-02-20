# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: saveReport.py
# @Author: chenzw
# @Institution: Guangzhou
# @E-mail: 2648738760@qq.com
# @Site: 
# @Time: 2月 17, 2023
# ---
from CommonFunc.httpRequests import httpReqHelp
from CommonFunc.readFIleContent import yamlHelp,TextHelp
import json
from CommonFunc.getTime import TimeHelp

class DailyTool:

    def __init__(self):
        self.http_help = httpReqHelp()
        self.yaml_help = yamlHelp()
        self.time_help = TimeHelp()
        self.env_data = self.yaml_help.yaml_read(r"F:\projectcodes\dingtalkFile\env_setting.yml")
        self.project_info = self.yaml_help.yaml_read(r"F:\projectcodes\dingtalkFile\project_info.yml")
        self.header = self.env_data["common_header"]
        self.cookie = self.env_data["cookie"]
        print(self.cookie)
        self.today_date = self.time_help.get_day_nowtime()

    def get_daily_today(self,begin_time=None,end_time=None):
        self.header["Cookie"] = self.cookie
        req_body = self.env_data["report_list_param"]
        if begin_time and end_time:
            req_body["workingHourDateBegin"]=begin_time
            req_body["workingHourDateEnd"]=end_time
        else:

            req_body["workingHourDateBegin"]=self.today_date
            req_body["workingHourDateEnd"]=self.today_date
        res = self.http_help.http_request(
            url=self.env_data["commonhost"]+self.env_data["report_list"]["path"],
            method=self.env_data["report_list"]["method"],
            headers=self.header,
            data=req_body
        )
        res_data = res.json()

        try:
            if res_data["success"]:
                res_data = res_data["data"]["total"],res_data["data"]["list"]
        except KeyError:
            print("获取日报列表失败，请查看响应信息！")

        return res_data
    def add_report(self,path):
        """
        path:txt的文件路径
        # task[subject_name,task_content,finished_rate,cost_time]
        """
        # 日报txt文件的内容
        task_list = TextHelp().read_all_file(path=path).split("\n")
        # yaml文件请求体
        input_data = self.env_data["save_param_single"]
        # 提交日期
        input_data["workingHourDate"]=self.today_date
        # 获取yaml文件每天任务信息
        task_content = self.env_data["work_content"]
        # 先去掉subjectWorkingHours在yaml文件的None内容
        input_data["subjectWorkingHours"].remove(None)
        if len(task_list)>1 and task_list[0]==self.today_date:
            print("start")
            for i in range(1,len(task_list)):
                task = task_list[i].split(":")
                print(task)
                # 根据项目名获取项目id,然后替换到请求体中的work_content
                task_content["subjectId"] = self.project_info[task[0]]
                # key值要递增
                task_content["key"] = "NEW_PROJECT_ID_"+str(i-1)
                # 项目名称
                task_content["subjectName"] = task[0]
                # 下面字段都是在workingHourList字段，字段的
                # 工作内容""
                task_content["workingHourList"][0]["taskName"] = task[1]
                # 完成程度
                task_content["workingHourList"][0]["completionRate"] = task[2]
                # 完成时间
                task_content["workingHourList"][0]["elapsedTime"]= task[3]
                # print(task_content)
                input_data["subjectWorkingHours"].append(task_content)
        print(input_data)
        # 接口发送请求
        self.header["Cookie"] = self.cookie
        res = self.http_help.http_request(
            url=self.env_data["commonhost"] + self.env_data["save_report"]["path"],
            method=self.env_data["save_report"]["method"],
            headers=self.header,
            data=input_data
        )
        print(res.json())



if __name__ == '__main__':
    dy_tool = DailyTool()
    # print(dy_tool.get_daily_today(begin_time='2023-02-16',end_time='2023-02-16'))
    # dy_tool.add_report()
    txt_path = r"C:\\Users\\86166\\Desktop\\每日任务.txt"
    b = dy_tool.add_report(txt_path)
    print(b)