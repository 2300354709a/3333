import unittest
import requests
from lib import db
from lib import load_data
import json
from conf import config


class TestUserReg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 整个测试类的准备方法
        cls.sheet = load_data.open_excel(config.data_file, "注册")

        def test_user_reg_normal(self):
            case_data = load_data.get_case(self.sheet, "test_user_reg_normal")
            url = case_data[2]
            data = json.loads(case_data[3])
            excepted_res = json.loads(case_data[4])

            res = requests.post(url=url, json=data)
            self.assertDictEqual(excepted_res, res.json())

            db.del_user("张三丰")  # 环境清理

    # def test_user_login_normal(self):
    # def test_user_reg_normal(self):
        # NAME = "张三丰"
        # if db.check_user(NAME):  # 环境准备
        #     db.del_user(NAME)
        # url = 'http://115.28.108.130:5000/api/user/reg/'
        # data = {"name": NAME, "password": "123456"}
        # res = requests.post(url=url, json=data)
        # self.assertEqual("成功", res.json()["msg"])
        # self.assertTrue(db.check_user(NAME))

        # db.del_user(NAME)   # 环境清理

    def test_user_reg_use_exist(self):
        url = 'http://115.28.108.130:5000/api/user/reg/'
        data = {"name": "张三", "password": "123456"}
        res = requests.post(url=url, json=data)
        self.assertEqual("失败，用户已存在", res.json()["msg"])