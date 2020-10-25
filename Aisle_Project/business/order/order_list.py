# -*- coding:utf-8 -*-
# Author:Queen_XTT

import requests
from config.url_config import admin_url, host, header_config
from common.log import Log
from common.url_module import query_module_url

log = Log()
import os

pyname = os.path.basename(__file__)

"""
订单模块的接口集合
"""
# 获取本业务url和host
url_order = admin_url.get("order", "")
header = header_config


# host = host.get("host", "") + module_url.get("admin", "")
# url_order = admin_url.get("order", "")


class Order_List():

    def create_order(self, body, app_id, number, fee_type, money, product_id, facility, device_type, header=None):
        """
        创建订单
        :param body: 备注
        :param app_id: API列表的APP_ID
        :param number: 订单号
        :param fee_type: 订单_币种
        :param money: 订单金额
        :param product_id: 聚合产品编号
        :param facility: 设备号
        :param device_type: 产品类型（"ios","android"）
        :param header:
        :return:
        """
        log.info("[ {} ------ create_order ------ start ]".format(pyname))
        url = host.get("host") + url_order.get("create_order", "")
        # 如果外部传入header就更新header的value
        if header:
            header_config['ffbodysign'] = header
        data = {
            "body": body,
            "attach": "test",
            "app_id": app_id,
            "nonce_str": "DBE40744-EF3363-65169-010204ED",
            "out_trade_no": number,
            "fee_type": fee_type,
            "total_fee": money,
            "time_start": None,
            "time_expire": None,
            "pay_product": product_id,
            "notify_url": "http://www.com",
            "trade_type": "MWEB",
            "user_uid": facility,
            "client_ip": facility,
            "device_id": facility,
            "device_type": device_type
        }
        response = requests.post(url=url, headers=header_config, json=data)
        log.info("[ {} ------ create_order ------ end ]".format(pyname))
        return response

    def get_order_data(self, module, token, role, picker, date_type, start_time, end_time, user_uid=None, status=None,
                       mchUserId=None, product_id=None, complained=None):
        """
        搜索订单数据
        :param picker: 时间
        :param date_type:  时间类型
        :param start_time: 开始时间
        :param end_time: 结束时间
        :param user_uid: 手机号(或其MD5值)
        :param status: 订单状态
        :param mchUserId:  商户编号
        :param product_id:  子通道编号
        :param complained:  投诉标记
        """
        log.info("[ {} ------ get_order_data ------ start ]".format(pyname))
        url = query_module_url(module) + url_order.get("order_list", "")
        data = {"userUid": user_uid, "subProductI": "", "status": status, "picker": picker,
                "lastly": "1d", "orderNo": None, "startTime": start_time, "aisleType": None, "mchUserId": mchUserId,
                "complained": complained, "endTime": end_time, "pageIndex": 1, "pageSize": 50, "dateType": date_type,
                "locale": "zh", "role": role, "subProductId": product_id}
        header["cookie"] = token
        response = requests.post(url=url, headers=header, json=data).json()
        # res = response["data"]["data"][0]
        # order_data = {
        #     "mchOrderNo": res["mchOrderNo"],
        #     "paymentId": res["paymentId"]
        # }
        # log.info("[ {} ------ get_order_data ------ end ]".format(pyname))
        # return order_data
        return response.get("data")

    def get_order_info(self, outTradeNo):
        """
        订单详情
        """
        url = host + url_order.get("order_info", "")
        data = {"outTradeNo": outTradeNo, "locale": "zh", "role": "administator"}
        response = requests.post(url=url, headers=header_config, json=data)
        return response


if __name__ == '__main__':
    from business.merchants.merchants_list import get_merchants_appid
