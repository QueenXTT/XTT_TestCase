# -*- coding:utf-8 -*-
# Author:Queen_XTT
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from business.module_process.mp_login import system_login
from business.module_process.mp_merchant import insert_merchants
from config.parameter_config import parameter
from config.url_config import module_url
from business.merchants.merchants_list import Merchants_List
from common.generate_random import test_generateRandom, generatorEmail
import unittest
from common.get_data_common import Get_Data

"""
用户登录_获取cookie
"""


class Test_Order(unittest.TestCase):

    def setUp(self):
        self.get_data = Get_Data()
        self.data = parameter
        self.admin = module_url.get("admin").split("/")[-1]
        self.merchant = module_url.get("merchant").split("/")[-1]
        self.app_name = test_generateRandom(parameter.get("m_app_name", ""), 9999, 4)  # 商户应用_名称
        self.m_name = test_generateRandom(parameter.get("merchants_name", ""), 9999, 4)  # 商户名称
        self.merchants = Merchants_List()
        self.email = generatorEmail()

    def test01_admin_login(self):
        """ 运营后台_登录 """
        admin_token = system_login(self.admin, self.data["user_name"], self.data["user_pwd"], self.data["secret_key"])
        # 写入token
        self.get_data.write_data(
            data={self.admin + "_token": admin_token.get("u_token", ""),
                  self.admin + '_role': admin_token.get("role", "")})

    @unittest.skip('test02_merchant_login')
    def test02_merchant_login(self):
        """ 新增商户/商户后台登录 """
        readdata = self.get_data.read_data()
        merchants_data = insert_merchants(self.admin, readdata.get(self.admin + '_token', ""), self.m_name, self.email,
                                          readdata.get(self.admin + "role", ""))  # 新增商户/搜索商户
        merchant_token = system_login(self.merchant, merchants_data["email"], merchants_data["password"])  # 新商户_登录
        readdata.update({self.merchant + "_token": merchant_token.get("u_token", ""),
                         self.merchant + "_role": merchant_token.get("role", "")})
        self.get_data.write_data(data=readdata)
        print(self.get_data.read_data())

    @unittest.skip('test03')
    def test03_select_merchant_app(self):
        readdata = self.get_data.read_data()
        print(self.merchants.get_merchants_appid(self.admin, readdata["admin_token"], appname=self.app_name))
        # print(get_merchants_appid(self.admin, admin_token, appname="testing_测试是"))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
