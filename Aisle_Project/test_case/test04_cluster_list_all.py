# -*- coding:utf-8 -*-
# Author:Queen_XTT
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest, random
from config.url_config import module_url
from common.get_data_common import Get_Data
from business.aisle_manage.cluster_list import query_cluster_list, add_cluster, edit_cluster
from config.parameter_config import parameter
from common.generate_random import test_generateRandom

"""
运营后台 - 通过管理/聚合通道 - 所有操作
"""


class Cluster_list_All(unittest.TestCase):

    def setUp(self):
        self.admin = module_url.get("admin").split("/")[-1]
        self.get_data = Get_Data()
        self.read_data = self.get_data.read_data()
        self.token = self.read_data.get(self.admin + "_token", "")
        self.role = self.read_data.get(self.admin + "_role", "")
        self.c_name = test_generateRandom(parameter.get("cluster_name", ""), 9999, 4)  # 聚合名称
        self.random_num = random.randint(1, 66)

    def test01_query_cluster(self):
        """ 聚合通道_初始页 """
        query_cluster_list(self.admin, self.token, self.role)

    def test02_add_cluster(self):
        """ 新增_聚合通道 """
        add_cluster(self.admin, self.token, self.role, self.c_name, self.random_num)
        global c_data
        c_data = query_cluster_list(self.admin, self.token, self.role, self.c_name).get("data")[-1]

    def test03_edit_cluster(self):
        """ 编辑_聚合通道 """
        edit_cluster(self.admin, self.token, self.role, c_data["productName"] + "编辑", c_data["productId"],
                     c_data["productCode"], self.random_num)
        query_cluster_list(self.admin, self.token, self.role, c_data["productName"] + "编辑")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
