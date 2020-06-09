# 导包
import unittest, logging

import app
from api.login_api import LoginApi

from utils import assert_common, read_login_data
from parameterized import parameterized


# 创建unittest的类
class TestIHRMLoginParams(unittest.TestCase):
    # 进行初始化
    def setUp(self):
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 定义登录数据文件的路径
    filepath = app.BASE_DIR + "/data/login_data.json"

    @parameterized.expand(read_login_data(filepath))
    # 编写登录成功函数
    def test01_login(self, case_name, request_body, success, code, message, http_code):
        # 使用封装的接口调用登录接口，并接收返回的响应数据
        response = self.login_api.login(request_body, {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("登录的结果为：{}".format(response.json()))
        assert_common(self, http_code, success, code, message, response)
