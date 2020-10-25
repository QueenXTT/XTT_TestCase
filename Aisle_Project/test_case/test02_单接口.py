# -*- coding:utf-8 -*-
# Author:Queen_XTT
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
from common.get_data_common import Get_Data
from business.order.order_list import Order_List
from ddt import ddt,unpack,data

"""
单接口
"""

excel_data = Get_Data().get_excel_data('../test_data/test_02.xlsx','order_list')
print(excel_data)


@ddt
class Test_Order(unittest.TestCase):

    def setUp(self):
        self.get_data = Get_Data()
        self.read_data = self.get_data.read_data()
        self.read_token = self.read_data['admin_token']


    # def test01_admin_login(self):
    #     """ 运营后台_登录 """
    #     token= self.read_data['admin_token']
    #     order_data = Order_List().get_order_data(token)
    #     assert type(order_data) == dict, '未获取到'


    @data(*excel_data)
    @unpack
    def test02_admin_login(self,apiname, token, mchUserId, orderNo, status, expect):
        """ 运营后台_登录 """
        token_ = self.read_token if token else token
        response = Order_List().get_order_data(token_, mchUserId, orderNo, status)
        # print(response)
        # print(expect)

        self.get_data.assert_repose(expect, response, expect)


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()