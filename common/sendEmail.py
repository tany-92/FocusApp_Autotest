# coding=utf-8

import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from common.readConfig import Readconfig
from common.logs import Log

conf = Readconfig()
log = Log()


class Email:

    def __init__(self):

        """
            从config配置文件中获取发送邮箱、接收邮箱
        """

        self.sender = conf.getemailValue('sender')
        self.receiver = conf.getemailValue('receiver')
        self.mail_host = conf.getemailValue('mail_host')
        self.mail_user = conf.getemailValue('mail_user')
        self.mail_pass = conf.getemailValue('mail_pass')


    def get_mail(self):

        """
            从report中获取最新一个测试报告，并返回body
        """

        PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
        report_path = PATH("D:\\study\\App-Test\\report")

        lists = os.listdir(report_path)
        lists.sort(key=lambda fn: os.path.getmtime(report_path+"/"+fn))

        report = os.path.join(report_path, lists[-1])
        file = open(report, 'rb')
        mail_body = file.read()
        file.close()

        return mail_body

    def send_mail(self):

        """
            发送测试报告
        """

        mail = self.get_mail()
        message = MIMEText(mail, 'html', 'utf-8')
        message['From'] = Header("ty", 'utf-8')
        # message['To'] = Header("圈圈", 'utf-8')
        message['Subject'] = Header('UI自动化测试报告', 'utf-8')


        try:
            server = smtplib.SMTP('smtp.126.com')  # 发件人第三方SMTP服务器，端口是465
            server.login(self.mail_user, self.mail_pass)
            server.sendmail(self.sender, self.receiver, message.as_string())
            server.quit()
            log.info('邮件发送成功')
        except smtplib.SMTPException:
            log.error('邮件发送失败')


if __name__ == '__main__':
    em = Email()
    em.get_mail()
    em.send_mail()




