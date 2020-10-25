# -*- coding:utf-8 -*-
# Author:Queen_XTT
from business.order.order_list import Order_List
from common.log import Log

log = Log()
import os

pyname = os.path.basename(__file__)

"""
创建订单_接口组合
"""

Order_List = Order_List()


def insert_order(body, app_id, number,fee_type, money, product_id, facility,device_type):
    """
    新增_订单
    :param body: 备注
    :param app_id: API列表的APP_ID
    :param number: 订单号
    :param fee_type: 订单_币种
    :param money: 订单金额
    :param product_id: 聚合产品编号
    :param facility: 设备号
    :param device_type: 订单手机类型
    :return:
    """
    log.info("[ {} ------ insert_order ------ start ]".format(pyname))
    oder_fail = Order_List.create_order(body, app_id, number, fee_type, money, product_id, facility, device_type)
    assert oder_fail.status_code == 200, '接口请求失败'
    ffbodysign = oder_fail.json().get('msg').split('实际签名为:')[1]
    oder_pass = Order_List.create_order(body, app_id, number, fee_type, money, product_id, facility, device_type,
                                        header=ffbodysign).json()
    assert oder_pass.get('msg').lower() == 'ok', oder_pass.get('msg')
    log.info("[ {} ------ insert_order ------ end ]".format(pyname))
