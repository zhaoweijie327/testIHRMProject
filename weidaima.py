# 需求：实现员工管理模块的登录
# 导包
import requests

# 发送IHRM登录的接口请求
response = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                         json={"mobile": "13800000002", "password": "123456"},
                         headers={"Content-Type": "application/json"})
# 查看登录的结果
print("登录的结果为：", response.json())