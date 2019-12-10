# 导包
import unittest

from tools.HTMLTestReportCN import HTMLTestRunner

# 定义测试套件
suite = unittest.defaultTestLoader.discover("./scripts")

# 获取报告存储文件流 并实例化HTMLTest
with open("./report/report.html","wb") as f:
    HTMLTestRunner(stream = f).run(suite)


