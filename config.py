import os
import logging
# 获取当前文件的绝对路径
# print(os.path.abspath(__file__))
# # 截取当前目录部分
# print(os.path.dirname(os.path.abspath(__file__)))
from logging.handlers import TimedRotatingFileHandler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 初始化日志配置
def init_log_config():
    # 创建日志器
    my_logger = logging.getLogger()
    # 设置日志输出级别
    my_logger.setLevel(logging.INFO)
    # 创建处理器  控制台--StreamHandler  时分文件---TimedRotatingFileHandler
    # -->控制台
    shl = logging.StreamHandler()
    # --->时分文件
    trfh = TimedRotatingFileHandler(BASE_DIR + "/./log/log.log",when="h",interval=1,backupCount=2,encoding="utf-8")
    # 创建格式化器
    fmter = logging.Formatter(fmt='%(asctime)s  %(levelname)s  [%(name)s]  [%(filename)s(%(funcName)s:%(lineno)d)]  -  %(message)s')
    # 处理器添加格式化器
    shl.setFormatter(fmter)
    trfh.setFormatter(fmter)
    # 日志器添加处理器
    my_logger.addHandler(shl)
    my_logger.addHandler(trfh)

init_log_config()