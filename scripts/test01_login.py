# 创建测试类
import unittest

import api
from api.api_login import ApiLogin
from tools.assert_common import assert_common


class TestLogin(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        # 获取ApiLogin对象
        cls.login = ApiLogin()

    # 登录测试方法
    def test_login(self,mobile = "13800000002",password = "123456"):
        response = self.login.api_login(mobile,password)
        print(response.json())  # 获取响应数据结果
        # 提取token
        token = response.json().get("data")
        api.headers["Authorization"] = "Bearer " + token
        print("登录成功后的headers值为:",api.headers)
        # 断言.
        assert_common(self,response)

