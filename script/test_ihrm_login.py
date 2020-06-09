# 导包
import unittest, logging
from api.login_api import LoginApi

from utils import assert_common


# 创建unittest的类
class TestIHRMLogin(unittest.TestCase):
    # 进行初始化
    def setUp(self):
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 编写登录成功函数
    def test01_login_success(self):
        # 使用封装的接口调用登录接口，并接收返回的响应数据
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("登录成功的结果为：{}".format(response.json()))
        assert_common(self, 200, True, 10000, "操作成功", response)

    # 实现手机号码为空
    def test02_mobile_is_empty(self):
        # 使用封装的接口调用登录接口，并接收返回的响应数据
        response = self.login_api.login({"mobile": "", "password": "error"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("手机号码为空的结果为：{}".format(response.json()))
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 手机号码不存在
    def test03_mobile_is_not_exists(self):
        # 使用封装的接口调用登录接口，并接收返回的响应数据
        response = self.login_api.login({"mobile": "13900000002", "password": "error"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("手机号码不存在的结果为：{}".format(response.json()))
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 密码错误
    def test04_password_is_error(self):
        # 使用封装的接口调用登录接口，并接收返回的响应数据
        response = self.login_api.login({"mobile": "13800000002", "password": "error"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("密码错误的结果为：{}".format(response.json()))
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 无参
    def test05_params_is_none(self):
        # 使用封装的接口调用登录接口，并接收返回的响应数据
        response = self.login_api.login({}, {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("无参的结果为：{}".format(response.json()))
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 传入Null
    def test06_params_is_null(self):
        # 使用封装的接口调用登录接口，并接收返回的响应数据
        response = self.login_api.login(None, {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("传入None的结果为：{}".format(response.json()))
        assert_common(self, 200, False, 99999, "抱歉，系统繁忙，请稍后重试！", response)

    # 多参
    def test07_more_params(self):
        # 使用封装的接口调用登录接口，并接收返回的响应数据
        response = self.login_api.login({"mobile": "13800000002", "password": "123456", "more_params": "1"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("多参的结果为：{}".format(response.json()))
        assert_common(self, 200, True, 10000, "操作成功", response)

    # 少参-缺少mobile
    def test08_less_params_mobile(self):
        # 使用封装的接口调用登录接口，并接收返回的响应数据
        response = self.login_api.login({"password": "123456", "more_params": "1"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("少参-缺少mobile的结果为：{}".format(response.json()))
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 少参-缺少Passowrd
    def test09_less_password(self):
        # 使用封装的接口调用登录接口，并接收返回的响应数据
        response = self.login_api.login({"mobile":"13800000002", "more_params": "1"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("少参-缺少Passowrd的结果为：{}".format(response.json()))
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 错误参数
    def test10_params_is_error(self):
        # 使用封装的接口调用登录接口，并接收返回的响应数据
        response = self.login_api.login({"mboile":"13800000002","password":"123456", "more_params": "1"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("错误参数的结果为：{}".format(response.json()))
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 密码为空
    def test11_password_is_empty(self):
        # 使用封装的接口调用登录接口，并接收返回的响应数据
        response = self.login_api.login({"mobile":"13800000002","password":"", "more_params": "1"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("密码为空的结果为：{}".format(response.json()))
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)