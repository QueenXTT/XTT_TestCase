# -*- Coding: UTF-8 -*-
# Author : Queen_XTT

from business.wms_project.auth_try import wms_auth_try
from business.order.order_list import create_myslq, create_order
from business.owms_project.receiving_order_list import gcreceiving_sign
from business.owms_project.container_list import container_create
from business.owms_pda_project.order_shelves_list import Order_Shelves_List
from business.owms_project.batch_log_list import inventory_batch_log

"""
入库单业务_方法合集
"""


class Receiving_Order_Flow():

    def create_receiving_order_auth(self, wms_cookies, owms_cookies):
        """
        创建入库单_获取【客户代码，箱号】
        """
        receiving_code = create_order()  # 创建并审核入库单_自发_标准_快递
        o_id = create_myslq(receiving_code)  # 链接数据库，获取 o_id
        wms_auth_try(o_id, wms_cookies)  # WMS_执行对应ID的WMS同步队列
        receiving_order = gcreceiving_sign(receiving_code, owms_cookies)  # 查询入库单_获取【客户代码，箱号】
        receiving_order["receiving_code"] = receiving_code
        receiving_order["o_id"] = o_id
        print(receiving_order)
        return receiving_order

    def receiving_confirm_receipt(self, re_code, sku, re_type, owms_pda_cookies, owms_cookies, box=None):
        """
        PDA_入库单_收货_上架
        :param re_code: 入库单_单号
        :param sku: 商品编号
        :param re_type: 签收类型 【 按箱签收为 1；批量签收为：2；】
        """
        order_shelves = Order_Shelves_List()  # 入库单签收模块
        if re_type == 1:
            order_shelves.validate_box(box, sku, re_type, owms_pda_cookies)  # 箱号/SKU_验证
        elif re_type == 2:
            order_shelves.validate_box(re_code, sku, re_type, owms_pda_cookies)  # 单号/SKU_验证
        order_shelves.get_sku_inventory(sku, owms_pda_cookies)  # 获取SKU库存
        container_code = container_create(owms_cookies)  # 创建拣货容器
        if re_type == 1:
            order_shelves.confirm_receipt(box, sku, container_code, re_code, re_type, owms_pda_cookies)  # PDA_收货
        elif re_type == 2:
            order_shelves.confirm_receipt(re_code, sku, container_code, re_code, re_type, owms_pda_cookies)  # PDA_收货
        order_shelves.get_received_log(owms_pda_cookies)  # PDA_收货验证
        order_shelves.check_container(container_code, owms_pda_cookies)  # 上架_检查容器
        order_shelves.press_sku(container_code, sku, owms_pda_cookies)  # 上架_检查SKU
        order_shelves.confirm_press(container_code, sku, owms_pda_cookies)  # 上架
        inventory_batch_log(re_code, owms_cookies)  # 批次日志_查询


if __name__ == '__main__':
    from business.login.login_list import project_login
