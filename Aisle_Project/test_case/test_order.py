# -*- coding:utf-8 -*-
# Author:Queen_XTT

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from business.module_process.mp_order import insert_order
import unittest

"""
订单用例
"""

# class Test_Order(unittest.TestCase):
#     """订单"""
#
#     def setUp(self):
#         pass
#
#     def test01(self):
#         """新增订单/搜索订单"""
#         insert_order("pdx-cs123", 99, 'android')
#
#     def test02(self):
#         """展示订单详情"""
#         insert_order("pdx-cs123", 99, 'android')
#
#     def tearDown(self):
#         pass


if __name__ == '__main__':
    unittest.main()