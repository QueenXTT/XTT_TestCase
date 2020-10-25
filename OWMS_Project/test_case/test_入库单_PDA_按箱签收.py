# -*- Coding: UTF-8 -*-
# Author : Queen_XTT
import unittest,os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from business.login.login_list import project_login
from business.order.order_list import create_myslq,create_order
from business.wms_project.auth_try import wms_auth_try
from business.owms_project.receiving_order_list import gcreceiving_sign
from business.owms_project.batch_log_list import inventory_batch_log

from config import parameter_config
from business.owms_pda_project.order_shelves_list import Order_Shelves_List
from business.owms_project.container_list import container_create

"""
入库单 - PDA - 按箱签收 - 流程
"""
class Receiving_Order_Process(unittest.TestCase):

    def setUp(self):
        self.wms_cookies = project_login("wms")
        self.owms_cookies = project_login("owms")
        self.owms_pda_cookies = project_login("owms_pda")
        self.order_shelves = Order_Shelves_List() # 入库单签收模块

    def test01_box_receiving_order(self):
        """ 按箱签收 - 箱号SKU """
        receiving_code = create_order() # 创建并审核入库单_自发_标准_快递
        o_id = create_myslq(receiving_code) # 链接数据库，获取 o_id
        wms_auth_try(o_id, self.wms_cookies) # WMS_执行对应ID的WMS同步队列
        receiving_order = gcreceiving_sign(receiving_code,self.owms_cookies) # 查询入库单_获取【客户代码，箱号】
        # receiving_order = {'customer_code': 'G898', 'box_nos': ['RVG898-201022-0022-1', 'RVG898-201022-0022-2']}
        num = 0
        for box in receiving_order.get("box_nos"):
            num += 1
            self.order_shelves.gcreceiving_sign(box,self.owms_pda_cookies)
            sku = receiving_order.get("customer_code")+"-"+(parameter_config.owms_project.get("sku_{}".format(num)))
            print(sku)
            self.order_shelves.validate_box(box, sku, self.owms_pda_cookies)
            self.order_shelves.get_sku_inventory(sku, self.owms_pda_cookies)
            container_code = container_create(self.owms_cookies) # 创建拣货容器
            self.order_shelves.confirm_receipt(box,sku,container_code,receiving_code,self.owms_pda_cookies) # PDA_收货
            # self.order_shelves.get_received_log(self.owms_pda_cookies) # PDA_收货验证
            self.order_shelves.check_container(container_code,self.owms_pda_cookies) # 上架_检查容器
            self.order_shelves.press_sku(container_code,sku,self.owms_pda_cookies) # 上架_检查SKU
            self.order_shelves.confirm_press(container_code,sku,self.owms_pda_cookies) # 上架
            inventory_batch_log(receiving_code,self.owms_cookies) # 批次日志_查询


    @unittest.skip('test02')
    def test02_op_merchant(self):
        """ 启用/禁用_商户状态 """

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
