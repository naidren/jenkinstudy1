# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: loggerAndEmail.py
# @Author: chenzw
# @Institution: Guangzhou
# @E-mail: 2648738760@qq.com
# @Site: 日志操作
# @Time: 5月
import logging
import smtplib
import sys,os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from CommonFunc.readFIleContent import yamlHelp,ConfHelp
from CommonFunc.transformPath import PathHelper
class LoggerHelp:
    def __init__(self, log_path):
        self.file_name = log_path
        self.logger = logging.getLogger()
        # 设置日志的级别
        self.logger.setLevel(logging.DEBUG)
        # 设置日志的格式与内容
        self.formatter = logging.Formatter('[%(asctime)s]-[%(filename)s]-[%(levelname)s]:%(message)s')

    def _console(self, level, message):
        # 创建一个FileHandler对象，把日志内容追加到末尾
        fh = logging.FileHandler(self.file_name, 'a', 'utf8')
        fh.setLevel(logging.DEBUG)
        # 设置文件内容的格式
        fh.setFormatter(self.formatter)
        # 将内容添加到日志文件
        self.logger.addHandler(fh)

        # 创建StreamHandler对象，把日志输出到控制台
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        # 避免日志输出重复
        self.logger.removeHandler(fh)
        self.logger.removeHandler(ch)
        fh.close()

    def info(self, message):
        """打印信息，程序不会中止"""
        self._console('info', message)

    def debug(self, message):
        """打印调试信息，程序不会中止"""
        self._console('debug', message)

    def warning(self, message):

        self._console('warning', message)

    def error(self, message):
        self._console('error', message)


class EmailHElp:
    path_help = PathHelper()
    # 邮箱账号和密码放在本地或者配置文件里
    data1 = yamlHelp().yaml_=read(r"F:\projectcodes\pwd\mail163.yml")
    conf_file = path_help.get_absolute_path("PycharmProjects\\intefaceItems\\petitionProject\\staticDatas\\配置参数\\login.ini")
    conf_help = ConfHelp(conf_file)
    def email_attachment(self, report_path):
        '''配置邮件服务器信息'''
        smtpserver = 'smtp.163.com'
        port = 25
        sender = self.data1["account"]
        pwd = self.data1["email_pwd"]
        # 接收方邮箱,多个账号时用英文分号隔开
        # receiver = self.data1["reciever"]
        receiver = self.conf_help.get_one_item(section="email_setting",item_key="receiver")

        # 创建邮件对象
        msg = MIMEMultipart()
        # 发送人、收件人、邮件的主题
        msg['from'] = sender
        # 有多个收件人时，以分号隔开
        msg['to'] = ';'.join(receiver)
        msg['subject'] = '这是{0}项目自动化测试报告，请查收（机器人发送请忽略）'.format(self.conf_help.get_one_item(section="email_setting",item_key="item_name"))

        # 读取测试报告内容
        with open(report_path, 'rb') as rf:
            body = rf.read()

        # 写邮件的正文
        mine_text = MIMEText(body, 'html', 'utf8')
        msg.attach(mine_text)

        # 写附件内容
        att = MIMEText(body, 'base64', 'utf8')
        att['Content-type'] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment;filename="%s"' % report_path
        msg.attach(att)

        # 发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, port)
        smtp.login(sender, pwd)
        smtp.sendmail(sender, receiver.split(';'), msg.as_string())
        smtp.close()
        print('发送邮件成功！')

# if __name__ == '__main__':
#
#     data1 = yamlHelp().yaml_read(r"F:\projectcodes\pwd\mail163.yml")
#     print(data1["email_pwd"])