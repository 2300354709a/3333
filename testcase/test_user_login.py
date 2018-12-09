import unittest
import requests
from lib import db
from lib import load_data
import json
from lib.case_log import case_log
from conf import config

class TestUserLogin(unittest.TestCase):
    @ classmethod
    def setUpClass(cls):  # 整个测试类的准备方法
        cls.sheet = load_data.open_excel(config.data_file, "登录")
    @unittest.skipUnless(db.check_user("张三"), "跳过该测试用例")
    def test_user_login_normal(self):
        # url = 'http://115.28.108.130:5000/api/user/login/'
        # data = {"name": "张三", "password": "123456"}
        # res = requests.post(url=url, data=data)
        # self.assertIn("登录成功", res.text)
        case_data = load_data.get_case(self.sheet, "test_user_login_normal")
        url = case_data[2]
        data = json.loads(case_data[3])
        res = requests.post(url=url, data=data)
        case_log("test_user_login_normal", url, case_data[3], case_data[4], res.text)

        # config.logging.info("接口地址:{}".format(json.jumps(data))
        # config.logging.info("请求数据:{}".format())
        # config.logging.info("期望结果:{}".format(json.dumps(excepted_res))
        # config.logging.info("实际结果：{}".format(res.text))
        # self.assertIn("登录成功", res.text)

    def test_user_login_password_wrong(self):
        url = 'http://115.28.108.130:5000/api/user/login/'
        data = {"name": "张三好", "password": "1234567"}
        res = requests.post(url=url, data=data)
        self.assertIn("用户名或密码错误", res.text)

if __name__ == "__main__":
    unittest.main(verbosity=2)