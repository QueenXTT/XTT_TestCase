# -*- coding:utf-8 -*-
# Author:Queen_XTT
import requests
from config.url_config import admin_url, header_config
from common.url_module import query_module_url
from common.log import Log

log = Log()
import os

pyname = os.path.basename(__file__)
"""
通道列表 和 子通道 的接口集合
"""

# 获取本业务url和host
url_aisle = admin_url.get("aisle", "")
header = header_config


class Aisle_List():

    def query_aisle_list(self, module, token, role, aisle_type=None, status=None):
        """
        通道列表_初始页
        """
        log.info("[ {} ------ query_aisle_list ------ start ]".format(pyname))
        url = query_module_url(module) + url_aisle.get("aisle_list", "")
        data = {"aisleType": aisle_type, "status": status, "pageIndex": 1, "pageSize": 10, "locale": "zh", "role": role}
        header["cookie"] = token
        response = requests.post(url=url, headers=header, json=data).json()
        assert len(response.get("data").get("data")) > 0, "运营后台，通道列表_查询失败\n" + str(response)
        log.info("[ {} ------ query_aisle_list ------ end ]\n".format(pyname))
        return response.get("data")

    def aisle_combo(self, module, token, all=None, a_name=None):
        """
        通道供应商_下拉框数据
        """
        log.info("[ {} ------ aisle_combo ------ start ]".format(pyname))
        url = query_module_url(module) + url_aisle.get("aisle_combo", "")
        url = url + "&all={}".format(all)
        header["cookie"] = token
        response = requests.get(url=url, headers=header).json()
        assert response.get('msg').lower() == '操作成功', response.get('msg')
        if all != None:

            log.info("[ {} ------ aisle_combo ------ end ]\n".format(pyname))
            aisle_data = {}
            if a_name != None:
                for aisle in response.get("data"):
                    for key, value in aisle.items():
                        if value == a_name:
                            aisle_data = aisle
            return aisle_data

    def delivery_product(self, module, token, role):
        """
        通道下发人_下拉框数据
        """
        log.info("[ {} ------ delivery_product ------ start ]".format(pyname))
        url = query_module_url(module) + url_aisle.get("delivery_product", "")
        data = {"userType": "12", "locale": "zh", "role": role}
        header["cookie"] = token
        response = requests.post(url=url, headers=header, json=data).json()
        assert response.get('msg').lower() == 'success', response.get('msg')
        log.info("[ {} ------ delivery_product ------ end ]\n".format(pyname))
        return response.get("data")

    def op_aisle_type(self, module, token, aisle_id, op_type):
        """
        启用/禁用_通道状态
        :param user_id: 通道_编号
        :param op_type: 通道_状态
        """
        log.info("[ {} ------ op_aisle_type ------ start ]".format(pyname))
        url = query_module_url(module) + url_aisle.get("op_aisle_type", "")
        url_param = {"aisleTypeId": aisle_id, "opType": op_type}
        header["cookie"] = token
        response = requests.get(url=url, params=url_param, headers=header).json()
        assert response.get('msg').lower() == '操作成功', response.get('msg')
        log.info("[ {} ------ op_aisle_type ------ end ]\n".format(pyname))

    def save_aisle_type(self, module, token, a_type, a_id, a_name, email, white, channels, role):
        """
        编辑_通道_白名单
        """
        log.info("[ {} ------ save_aisle_type ------ start ]".format(pyname))
        url = query_module_url(module) + url_aisle.get("save_aisle_type", "")
        data = {"aisleType": a_type, "aisleName": a_name, "deliverierUsers": email, "whiteList": white,
                "channels": channels, "aisleId": a_id, "locale": "zh", "role": role}
        header["cookie"] = token
        response = requests.post(url=url, headers=header, json=data).json()
        assert response.get('msg').lower() == 'success', response.get('msg')
        log.info("[ {} ------ save_aisle_type ------ end ]\n".format(pyname))

    def query_assurer_combox(self, module, token):
        """
        查询_成员组合
        """
        log.info("[ {} ------ query_assurer_combox ------ start ]".format(pyname))
        url = query_module_url(module) + url_aisle.get("query_assurer_combox", "")
        header["cookie"] = token
        response = requests.get(url=url, headers=header).json()
        assert response.get('msg').lower() == 'success', response.get('msg')
        log.info("[ {} ------ query_assurer_combox ------ end ]\n".format(pyname))
        return response.get("data")

    def pay_product_list(self, module, token, role, aisle_type=None, product_name=None):
        """
        子通道列表_初始页
        """
        log.info("[ {} ------ pay_product_list ------ start ]".format(pyname))
        url = query_module_url(module) + url_aisle.get("pay_product_list", "")
        data = {"aisleType": aisle_type, "productName": product_name, "pageIndex": 1, "pageSize": 10, "locale": "zh",
                "role": role}
        header["cookie"] = token
        response = requests.post(url=url, headers=header, json=data).json()
        assert len(response.get("data").get("data")) > 0, "运营后台，通道列表_查询失败\n" + str(response)
        log.info("[ {} ------ pay_product_list ------ end ]\n".format(pyname))
        return response.get("data").get("data")[-1]

    def aisle_order(self, module, token, role, product_id):
        """
        测试（通道_订单）
        """
        log.info("[ {} ------ aisle_order ------ start ]".format(pyname))
        url = query_module_url(module) + url_aisle.get("aisle_order", "")
        data = {"productId": product_id, "locale": "zh", "role": role}
        header["cookie"] = token
        response = requests.post(url=url, headers=header, json=data).json()
        assert response.get('msg').lower() == 'success', response.get('msg')
        log.info("[ {} ------ aisle_order ------ end ]\n".format(pyname))

    def aisle_channel(self, module, token, aisle_id):
        """
        相关的_子通道
        :param user_id: 通道_编号
        """
        log.info("[ {} ------ aisle_channel ------ start ]".format(pyname))
        url = query_module_url(module) + url_aisle.get("aisle_channel", "")
        url_param = {"aisleTypeId": aisle_id}
        header["cookie"] = token
        response = requests.get(url=url, params=url_param, headers=header).json()
        assert response.get('msg').lower() == '操作成功', response.get('msg')
        log.info("[ {} ------ aisle_channel ------ end ]\n".format(pyname))

    def save_product(self, module, token, p_id, p_name, aisle_type, code, p_code, role, cost=None, pay_money=None,
                     warning=None):
        """
        编辑_子通道
        :param p_id: 子通道编号
        :param p_name: 子通道名
        :param aisle_type: 通道类型（父级）
        :param code: 支付方式
        :param p_code: 子通道_编码
        :param cost: 成本
        :param pay_money: 支付金额
        :param warning: 预警额度
        """
        log.info("[ {} ------ save_product ------ start ]".format(pyname))
        url = query_module_url(module) + url_aisle.get("save_product", "")
        data = {"productId": p_id, "productName": p_name, "aisleType": aisle_type, "channelCode": code,
                "otcUserId": "", "costChargeRate": cost, "amountLimit": pay_money, "productCode": p_code,
                "warningLines": warning, "remark": "", "locale": "zh", "role": role}
        header["cookie"] = token
        response = requests.post(url=url, headers=header, json=data).json()
        assert response.get('msg').lower() == '操作成功', response.get('msg')
        log.info("[ {} ------ save_product ------ end ]\n".format(pyname))

    def op_product_credit(self, module, token, role, product_id,alter_fee):
        """
        编辑_授信额度
        :param product_id: 子通道ID
        :param alter_fee: 授信额度
        """
        log.info("[ {} ------ up_product_credit ------ start ]".format(pyname))
        url = query_module_url(module) + url_aisle.get("up_product_credit", "")
        data = {"productId":product_id,"alterFee":alter_fee,"locale":"zh","role":role}
        header["cookie"] = token
        response = requests.post(url=url, headers=header, json=data).json()
        assert response.get('msg').lower() == 'success', response.get('msg')
        log.info("[ {} ------ up_product_credit ------ end ]\n".format(pyname))

    def op_pay_product(self, module, token, product_id, op_type):
        """
        启用/禁用_子通道状态
        :param product_id: 子通道_编号
        :param op_type: 通道_状态
        """
        log.info("[ {} ------ op_pay_product ------ start ]".format(pyname))
        url = query_module_url(module) + url_aisle.get("op_pay_product", "")
        url_param = {"productId": product_id, "opType": op_type}
        header["cookie"] = token
        response = requests.get(url=url, params=url_param, headers=header).json()
        assert response.get('msg').lower() == '操作成功', response.get('msg')
        log.info("[ {} ------ op_pay_product ------ end ]\n".format(pyname))

if __name__ == '__main__':
    print("sss")