# -*- coding:utf-8 -*-
# Author:Queen_XTT
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
from config.url_config import module_url
from common.get_data_common import Get_Data
from business.merchants.merchants_list import Merchants_List
from config.parameter_config import parameter
from business.module_process.mp_login import system_login
from common.url_module import request_page

"""
运营后台 - 商户管理/商户列表 - 所有操作
"""


class Merchant_List_All(unittest.TestCase):

    def setUp(self):
        self.admin = module_url.get("admin").split("/")[-1]
        self.merchant = module_url.get("merchant").split("/")[-1]
        self.get_data = Get_Data()
        self.read_data = self.get_data.read_data()
        self.token = self.read_data.get(self.admin + "_token", "")
        self.role = self.read_data.get(self.admin + "_role", "")
        self.m_name = parameter.get("merchants_name", "XTT")
        self.merchants = Merchants_List()

    def test01_update_Merchant(self):
        """ 编辑商户_验证 """
        first_data = self.merchants.get_merchants(self.admin, self.token, self.role, self.m_name).get("data")
        self.merchants.get_allcoin_list(self.admin, self.token)
        page = request_page(first_data.get("totalCount"), first_data.get("pageSize"))
        global m_data
        m_data = \
        self.merchants.get_merchants(self.admin, self.token, self.role, self.m_name, page=page).get("data").get("data")[
            -1]
        self.merchants.save_merchant(self.admin, self.token, m_data["merchantName"] + "编辑", m_data["merchantAccount"],
                                     m_data["supportCoinList"], self.role, m_data["userId"], m_data["merchantId"], 100)
        m_data_s = \
        self.merchants.get_merchants(self.admin, self.token, self.role, account=m_data["merchantAccount"]).get(
            "data").get(
            "data")[0]
        assert m_data_s.get('merchantName') != m_data.get('merchantName'), "编辑前：" + m_data.get(
            'merchantName') + "\n编辑后：" + m_data_s.get('merchantName') + "\n商户列表操作编辑，验证失败"

    # @unittest.skip('test02')
    def test02_op_merchant(self):
        """ 启用/禁用_商户状态 """
        if m_data["status"] != 1:
            self.merchants.op_merchant(self.admin, self.token, 1, m_data["userId"])  # 启用_商户
        else:
            self.merchants.op_merchant(self.admin, self.token, 0, m_data["userId"])  # 禁用_商户
            self.merchants.op_merchant(self.admin, self.token, 1, m_data["userId"])  # 启用_商户

    def test03_merchant_pwd(self):
        """ 重置_商户密码 """
        # global merchant_pwd
        merchant_pwd = self.merchants.reset_merchant_pwd(self.admin, self.token, m_data["userId"])
        system_login(self.merchant, merchant_pwd["email"], merchant_pwd["password"])

    def test04_merchant_google(self):
        """ 重置_谷歌验证码 """
        self.merchants.reset_merchant_google(self.admin, self.token, m_data["userId"], self.role)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
