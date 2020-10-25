# -*- Coding: UTF-8 -*-
# Author: Queen_XTT
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest, random, time
from business.aisle_manage.merchant_aisle_list import query_cluster_combox, cluster_list, son_product_list, \
    batch_merchant_config
from common.generate_random import test_generateRandom
from common.get_data_common import Get_Data
from business.merchants.merchants_list import Merchants_List
from config.parameter_config import parameter
from business.aisle_manage.cluster_list import query_cluster_list
from config.url_config import module_url, host
from common.url_module import request_page
from business.aisle_manage.aisle_list import Aisle_List
from business.module_process.mp_order import insert_order
from common.get_local_ip import get_local_ip
from business.module_process.mp_merchant import random_all_coin
from business.order.order_list import Order_List

"""
运营后台 - 通道管理/商户通道 - 配置操作
"""


class Aisle_List_All(unittest.TestCase):
    def setUp(self):
        self.merchants = Merchants_List()
        self.aisle = Aisle_List()
        self.order = Order_List()
        self.admin = module_url.get("admin").split("/")[-1]
        self.get_data = Get_Data()
        self.read_data = self.get_data.read_data()
        self.token = self.read_data.get(self.admin + "_token", "")
        self.role = self.read_data.get(self.admin + "_role", "")
        self.m_name = parameter.get("merchants_name", "XTT")  # 商户名称
        self.c_name = parameter.get("cluster_name", "XTT")  # 聚合通道名称
        self.a_name = parameter.get("aisle_name", "XTT")  # 下单的通道名称
        self.subset_name = parameter.get("aisle_xtt", "XTT")  # 子通道名称
        self.num = random.randint(1, 10)
        self.number = test_generateRandom("XTT_", 999999999999, 12)  # 订单号
        self.facility = test_generateRandom("XTT_", 999999, 6)  # 设备号
        self.start_time = int(round(time.time() * 1000))  # 开始时间
        time_local = time.strftime('%Y-%m-%d', time.localtime(time.time())) + " 23:59:59"
        timeArray = time.strptime(time_local, "%Y-%m-%d %H:%M:%S") # 转换成时间数组
        self.end_time = int(round(time.mktime(timeArray) * 1000))  # 结束时间（时间戳格式）

    def test01_aisle_prepare(self):
        """ 商户通道_预备接口"""
        first_data = self.merchants.get_merchants(self.admin, self.token, self.role, self.m_name).get("data")
        page = request_page(first_data.get("totalCount"), first_data.get("pageSize"))
        global m_data  # 商户数据
        m_data = \
            self.merchants.get_merchants(self.admin, self.token, self.role, self.m_name, page=page).get("data").get(
                "data")[
                -1]
        print(m_data)
        c_count = query_cluster_list(self.admin, self.token, self.role).get("totalCount")
        c_data = query_cluster_list(self.admin, self.token, self.role, size=c_count).get("data")
        cluster_all = {}  # 聚合通道数据
        for cluster in c_data:
            for key, value in cluster.items():
                if self.c_name in str(value):
                    cluster_all = cluster
        global cluster_data
        cluster_data = cluster_all
        print(cluster_data)
        a_combo = self.aisle.aisle_combo(self.admin, self.token, 1, self.a_name)
        print(a_combo)
        global product_list  # 子通道数据
        product_list = self.aisle.pay_product_list(self.admin, self.token, self.role, a_combo.get("aisleType"),
                                                   self.subset_name)
        print(product_list)

    # @unittest.skip('test02')
    def test02_query_cluster_ombox(self):
        """ 商户通道_配置初始页 """
        query_cluster_combox(self.admin, self.token, self.role)
        cluster_list(self.admin, self.token, cluster_data.get("productId"))
        son_product_list(self.admin, self.token, self.role, cluster_data.get("productId"), m_data.get("userId"))

    # @unittest.skip('test03')
    def test03_batch_config(self):
        """ 商户通道_配置 """
        mch_list = [{"mchUserId": m_data.get("userId"), "serviceChargeRate": self.num}]
        p_list = [{"aisleType": product_list.get("aisleType"), "channelCode": product_list.get("channelCode"),
                   "costChargeRate": self.num, "initialized": True, "productCode": product_list.get("productCode"),
                   "productId": product_list.get("productId")}]
        batch_merchant_config(self.admin, self.token, self.role, cluster_data.get("productId"), mch_list, p_list)

    def test04_add_order(self):
        """ 新增订单_验证 """
        app_data = self.merchants.get_merchants_appid(self.admin, self.token, self.role, m_data.get("userId"))
        # app_data = self.merchants.get_merchants_appid(self.admin, self.token, self.role, 11240)
        print(app_data)
        if app_data.get("totalCount") > 0:
            api_info = app_data.get("data")[-1]
        else:
            """ 新增API应用/搜索API应用 """
            local_ip = get_local_ip()
            coin_list = random_all_coin(self.admin, self.token, count=2, mch_user_id=m_data.get("userId"))
            # random(coin_list)
            self.merchants.save_merchant_app(self.admin, self.token, self.role, m_data.get("userId"), test_generateRandom(self.m_name, 9999, 4),
                                             host.get("host"), coin_list, local_ip.get("ip"))
            api_data = self.merchants.get_merchants_appid(self.admin, self.token, self.role, m_data.get("userId"),
                                                          self.m_name, local_ip.get("ip"))
            api_info = api_data.get("data")[-1]
        print(api_info)

        coin = random.choice(api_info.get("supportCoinList"))
        device_type = random.choice(["ios", "android"])  # 产品类型
        insert_order("XTT_新增订单", api_info.get("appId"), self.number, coin, self.num, cluster_data.get("productCode"),
                     self.facility, device_type)
        oreder_info = self.order.get_order_data(self.admin, self.token, self.role, [self.start_time, self.end_time], 1,
                                  self.start_time, self.end_time, mchUserId=m_data.get("userId"),
                                  product_id=product_list.get("productId"))
        print(oreder_info)
        assert oreder_info.get("totalCount") > 0, '订单接口，搜索无数据'.format(oreder_info.get("data"))



    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
