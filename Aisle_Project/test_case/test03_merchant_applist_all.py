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
from common.url_module import request_page
from common.get_local_ip import get_local_ip

"""
运营后台 - 商户管理/API列表 - 所有操作
"""


class Merchant_APPList_All(unittest.TestCase):

    def setUp(self):
        self.admin = module_url.get("admin").split("/")[-1]
        self.get_data = Get_Data()
        self.read_data = self.get_data.read_data()
        self.token = self.read_data.get(self.admin + "_token", "")
        self.role = self.read_data.get(self.admin + "_role", "")
        self.m_name = parameter.get("merchants_name", "XTT")
        self.merchants = Merchants_List()

    def test01_select_app(self):
        """ 查询_API列表 """
        self.merchants.mch_combo_list(self.admin, self.token)
        first_app = self.merchants.get_merchants_appid(self.admin, self.token, self.m_name)
        assert first_app["data"]["data"] > 0, first_app.get('msg')
        page = request_page(first_app.get("totalCount"), first_app.get("pageSize"))
        global app_list
        app_list = self.merchants.get_merchants_appid(self.admin, self.token, self.m_name, page=page).get("data")[-1]
        # print(app_list)

    @unittest.skip('test02')
    def test02_op_app(self):
        """ 启用/禁用_商户状态 """
        if app_list["status"] != 1:
            self.merchants.op_app(self.admin, self.token, app_list.get("appId"), 1)  # 启用_商户
        else:
            self.merchants.op_app(self.admin, self.token, app_list.get("appId"), 0)  # 禁用_商户
            self.merchants.op_app(self.admin, self.token, app_list.get("appId"), 1)  # 启用_商户

    @unittest.skip('test03')
    def test03_update_app(self):
        """ 编辑_API列表数据 """
        local_ip = get_local_ip()
        self.merchants.update_app(self.admin, self.token, app_list.get("appId"), local_ip.get("ip"), self.role)
        self.merchants.get_merchants_appid(self.admin, self.token, app_list.get("merchantName"),
                                           app_list.get("appName"), local_ip.get("ip"))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
