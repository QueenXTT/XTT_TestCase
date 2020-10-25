# -*- coding:utf-8 -*-
# Author:Queen_XTT
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from business.module_process.mp_login import system_login
from business.module_process.mp_merchant import insert_merchants,insert_merchants_app
from config.parameter_config import parameter
from business.merchants.merchants_list import Merchants_List
from common.generate_random import test_generateRandom,generatorEmail
import unittest
from common.get_data_common import Get_Data

"""
系统流程
"""
class Test_Order(unittest.TestCase):

    def setUp(self):
        self.get_data = Get_Data()
        self.data = parameter
        self.module = {
            "admin" : "admin",
            "merchant" : "merchant"
        }
        self.app_name = test_generateRandom(parameter.get("m_app_name", ""), 9999, 4)  # 商户应用_名称
        self.m_name = test_generateRandom(parameter.get("merchants_name", ""), 9999, 4)  # 商户名称
        self.email = generatorEmail()

    def test01_admin_login(self):
        """ 运营后台_登录 """
        # 测试
        admin_token = system_login(self.module["admin"],self.data["user_name"], self.data["user_pwd"], self.data["secret_key"])
        print(admin_token)
        # 写入token
        self.get_data.write_data(data={self.module["admin"]+'_token':admin_token})
        print("111111111")

    @unittest.skip('test02_merchant_login')
    def test02_merchant_login(self):
        """ 新增商户/商户后台登录 """

        merchants_data = insert_merchants(self.module["admin"], self.m_name, self.email) # 新增商户/搜索商户
        merchant_token = system_login(self.module["merchant"], merchants_data["email"], merchants_data["password"]) # 新商户_登录
        print('merchant_token:  ',merchant_token)

        readdata = self.get_data.read_data()
        readdata.update({self.module["merchant"]+'_token':merchant_token})
        self.get_data.write_data(data=readdata)
        print("222222222222")

        # self.app_name = insert_merchants_app(self.module["merchant"],self.app_name) # 新增商户应用

    @unittest.skip('test03')
    def test03_select_merchant_app(self):
        print("3333333333333")
        readdata = self.get_data.read_data()
        # print(get_merchants_appid(self.module["admin"], readdata['admin_token'], appname=self.app_name))
        # print(get_merchants_appid(self.module["admin"], admin_token, appname="testing_测试是"))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()