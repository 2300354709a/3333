
# 数据库配置
db_host = '115.28.108.130'
db_port = 3306
db_user = 'test'
db_password = '123456'
db = 'api_test'
# 日志使用
# level critical 严重问题
# error出错
# warning警告
# info:正常输出消息
# debug:调试信息

# #log 配置
# import logging.basicConfig(level=logging.DEBUG,
#     format="%(asctime)s %(levelname)s %(funcName)s[%(filename)s-%(lineno)d]%(message)s"
#     datefmt="%Y-%m-%d %H:%M:%S"#大写的，调试级别 大于等于指定级别都能输出 ERROR 这种则info级别的输出不了 %年
#     filename="../log/log.txt",
#     filemode='a'
#
# if __name__=="__main__":
#    logging.info("1")

import os
config_path=os.path.abspath(__file__)#__file__当前文件os.path.abspath()绝对路径
conf_path=os.path.dirname(config_path)#os.path.dirname()所在文件夹
project_path=os.path.dirname(conf_path)#项目绝对路径
# project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__内置路径
# print(project_path)
#数据文件目录
#data_path=os.path.join(project_path,'dara','data.xlsx')
report_file=os.path.join(project_path,'report','report.html')
data_file=os.path.join(project_path,'data',"ccc.xlsx")
log_file=os.path.join(project_path,'log',"log.txt")

import  logging

logging.basicConfig(level=logging.DEBUG,
                    format = "%(asctime)s %(levelname)s %(funcName)s [%(filename)s-%(lineno)d] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename=log_file)
                    # filemode="a")


#邮件配置
smtp_server = 'smtp.163.com'
smtp_user = 'ivan-me@163.com'
smtp_password = 'hanzhichao123'

receiver="cuperhin@126.com"
subject="接口测试报告"
body="hi,all,\n附件中是接口测试报告请查收."