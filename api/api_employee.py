
# 创建添加员工测试类
import requests

import api


class ApiEmployee:
    # 初始化
    def __init__(self):
        # 新增员工url
        self.url_add = api.BASE_URL + "/api/sys/user"
        # 修改,删除  通用url 提示 --->{}解决不同参数问题
        # {}为占位符  引用-->.foramt(user_id)
        self.url_emp = api.BASE_URL + "/api/sys/user/{}"
    # 新增员工
    def api_add_employee(self,username,mobile,workNumber):

        # 定义data数据
        data = {"username":username,
                "mobile": mobile,
                "workNumber": workNumber}

        # 调用post方法   必须返回return
        return requests.post(url = self.url_add,json=data,headers=api.headers)

    # 修改员工
    def api_put_employee(self,username):
        data = {"username":username}
        return requests.put(url=self.url_emp.format(api.user_id),json = data,headers = api.headers)

    # 查询员工
    def api_get_employee(self):
        return requests.get(url = self.url_emp.format(api.user_id),headers = api.headers)

    # 删除员工  ---> 调用delete方法
    def api_delete_employee(self,user_id):
        return requests.delete(url=self.url_emp.format(user_id),headers = api.headers)