# -*- Coding: UTF-8 -*-
# Author: Queen_XTT
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import random,unittest
from business.aisle_manage.aisle_list import Aisle_List
from common.generate_random import test_generateRandom
from common.get_data_common import Get_Data
from common.get_local_ip import get_local_ip
from config.parameter_config import parameter
from config.url_config import module_url

"""
运营后台 - 通道管理/通道列表 - 所有操作
"""


class Aisle_List_All(unittest.TestCase):

    def setUp(self):
        self.aisle = Aisle_List()
        self.admin = module_url.get("admin").split("/")[-1]
        self.get_data = Get_Data()
        self.read_data = self.get_data.read_data()
        self.token = self.read_data.get(self.admin + "_token", "")
        self.role = self.read_data.get(self.admin + "_role", "")
        self.subset_name = test_generateRandom(parameter.get("aisle_xtt", ""), 9999, 4)  # 子通道名称
        # self.subset_name = parameter.get("aisle_xtt", "")  # 子通道名称
        self.random_num = random.randint(1111, 9999)

    def test01_query_aisle(self):
        """ 通道列表_初始页 """
        global a_combo
        a_combo = self.aisle.aisle_combo(self.admin, self.token, 1, parameter.get("aisle_name"))
        # print(a_combo)
        global aisle_data
        aisle_data = \
            self.aisle.query_aisle_list(self.admin, self.token, self.role, a_combo.get("aisleType")).get("data")[-1]
        # print(aisle_data)
        self.aisle.delivery_product(self.admin, self.token, self.role)

    @unittest.skip('test02')
    def test02_op_aisle_type(self):
        """ 启用/禁用_通道状态 """
        if a_combo.get("disable"):
            self.aisle.op_aisle_type(self.admin, self.token, a_combo.get("aisleId"), 1)  # 启用_商户
        else:
            self.aisle.op_aisle_type(self.admin, self.token, a_combo.get("aisleId"), 0)  # 禁用_商户
            self.aisle.op_aisle_type(self.admin, self.token, a_combo.get("aisleId"), 1)  # 启用_商户

    @unittest.skip('test03')
    def test03_save_aisle_type(self):
        """ 编辑_通道列表数据 """
        local_ip = get_local_ip()
        channels = aisle_data.get("channels")
        channels.append({"channelCode": self.random_num, "channelName": self.subset_name, "supportDevice": ""})
        self.aisle.save_aisle_type(self.admin, self.token, a_combo.get("aisleType"), a_combo.get("aisleId"),
                                   a_combo.get("aisleName"), aisle_data.get("deliverierUser"), local_ip.get("ip"),
                                   channels, self.role)
        aisle_list = \
            self.aisle.query_aisle_list(self.admin, self.token, self.role, a_combo.get("aisleType")).get("data")[-1]
        assert aisle_list.get('whiteList') == local_ip.get("ip"), "编辑前：" + aisle_data.get(
            'whiteList') + "\n编辑后：" + aisle_list.get('whiteList') + "\n通道列表操作：编辑白名单，验证失败"

    def test04_query_aisle_subset(self):
        """ 子通道列表_初始页 """
        self.aisle.aisle_combo(self.admin, self.token)
        self.aisle.query_assurer_combox(self.admin, self.token)
        global product_list
        product_list = self.aisle.pay_product_list(self.admin, self.token, self.role, a_combo.get("aisleType"),
                                                   self.subset_name)
        # print(product_list)

    def test05_aisle_order(self):
        """ 测试（通道_订单） """
        self.aisle.aisle_order(self.admin, self.token, self.role, product_list.get("productId"))

    def test06_op_aisle_type(self):
        """ 编辑_子通道 """
        self.aisle.aisle_channel(self.admin, self.token, product_list.get("productId"))
        self.aisle.save_product(self.admin, self.token, product_list.get("productId"),
                                product_list.get("productName") + "编辑", a_combo.get("aisleType"),
                                product_list.get("channelCode"), product_list.get("productCode"), self.role,3)

    def test06_product_credit(self):
        """ 编辑_授信额度 """
        self.aisle.op_product_credit(self.admin, self.token, self.role, product_list.get("productId"), self.random_num)
        p_data = self.aisle.pay_product_list(self.admin, self.token, self.role, a_combo.get("aisleType"),
                                             self.subset_name)
        alter_fee = product_list.get('leftCreditFee') + self.random_num
        assert p_data.get('leftCreditFee') == alter_fee, "编辑前{}：".format(
            product_list.get('leftCreditFee')) + "\n编辑后{}：".format(alter_fee) + "\n子通道列表操作：编辑授信额度，验证失败"

    def test07_op_product_type(self):
        """ 启用/禁用_子通道状态 """
        if product_list.get("disable"):
            self.aisle.op_pay_product(self.admin, self.token, product_list.get("productId"), 1)  # 启用_商户
        else:
            self.aisle.op_pay_product(self.admin, self.token, product_list.get("productId"), 0)  # 禁用_商户
            self.aisle.op_pay_product(self.admin, self.token, product_list.get("productId"), 1)  # 启用_商户

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
