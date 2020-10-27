# -*- Coding: UTF-8 -*-
# Author : Queen_XTT
import unittest, os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from business.login.login_list import project_login
from business_flow.receiving_order_flow import Receiving_Order_Flow
from config import parameter_config
from business.owms_pda_project.order_shelves_list import Order_Shelves_List

"""
入库单 - PDA - 按箱签收 - 流程
"""


class Receiving_Order_Process(unittest.TestCase):

    def setUp(self):
        self.re_order_flow = Receiving_Order_Flow()
        self.wms_cookies = project_login("wms")
        self.owms_cookies = project_login("owms")
        self.owms_pda_cookies = project_login("owms_pda")
        self.order_shelves = Order_Shelves_List()  # 入库单签收模块

    def test01_box_receiving_order(self):
        """ 按箱签收 - 箱号SKU """
        re_order = self.re_order_flow.create_receiving_order_auth(self.wms_cookies, self.owms_cookies)
        # receiving_order = {'customer_code': 'G898', 'box_nos': ['RVG898-201022-0022-1', 'RVG898-201022-0022-2']}
        self.order_shelves.batch_sign(re_order.get("receiving_code"), self.owms_pda_cookies)  # 批量签收_签收
        num = 0
        for box in re_order.get("box_nos"):
            num += 1
            sku = re_order.get("customer_code") + "-" + (
                parameter_config.owms_project.get("sku_{}".format(num)))  # 商品编号
            self.re_order_flow.receiving_confirm_receipt(re_order.get("receiving_code"), sku, re_type=1,
                                                         owms_pda_cookies=self.owms_pda_cookies,
                                                         owms_cookies=self.owms_cookies, box=box)

    @unittest.skip('test02')
    def test02_op_merchant(self):
        """ 启用/禁用_商户状态 """

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
