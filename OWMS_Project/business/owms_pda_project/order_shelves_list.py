# -*- Coding: UTF-8 -*-
# Author : Queen_XTT
import requests
from config.url_config import owms_pda_url, host, login_header
from common.log import Log
log = Log()
import os,time
pyname = os.path.basename(__file__)
# 获取本业务url和host
owms_pda_url_sign = owms_pda_url.get("order_shelves", "")

"""
入库单_签收模块_接口集合
"""
class Order_Shelves_List():

    def gcreceiving_sign(self,box,header=None):
        """
        OWMS-PDA-按箱签收-签收
        """
        log.info("[ {} ------ gcreceiving_sign ------ start ]".format(pyname))
        url = host.get("owms_host") + owms_pda_url_sign.get("press_box_sign", "")
        # 如果外部传入header就更新配置中header的value
        if header:
            login_header['Cookie'] = header
        data = { "box": box }
        response = requests.post(url=url, headers=login_header, data=data).json()
        assert response.get("status") == 1, response.get("info")
        log.info("[ {} ------ gcreceiving_sign ------ end ]\n".format(pyname))

    def validate_box(self,box,sku,header=None):
        """
        OWMS-PDA-收货-箱号/SKU验证
        """
        log.info("[ {} ------ validate_box ------ start ]".format(pyname))
        url = host.get("owms_host") + owms_pda_url_sign.get("validate_box", "")
        # 如果外部传入header就更新配置中header的value
        if header:
            login_header['Cookie'] = header
        data = {
            "type": "sku",
            "box": box,
            "sku": sku,
            "relaType": 1
        }
        response = requests.post(url=url, headers=login_header, data=data).json()
        assert response.get("status") == 1, response.get("info")
        log.info("[ {} ------ validate_box ------ end ]\n".format(pyname))

    def get_sku_inventory(self, sku, header=None):
        """
        OWMS-PDA-收货-获取SKU库存
        """
        log.info("[ {} ------ get_sku_inventory ------ start ]".format(pyname))
        url = host.get("owms_host") + owms_pda_url_sign.get("get_sku_inventory", "")
        # 如果外部传入header就更新配置中header的value
        if header:
            login_header['Cookie'] = header
        data = { "product_barcode": sku }
        response = requests.post(url=url, headers=login_header, data=data).json()
        assert response.get("state") == 1, response.get("info")
        log.info("[ {} ------ get_sku_inventory ------ end ]\n".format(pyname))

    def confirm_receipt(self, box, sku, c_code, r_code, header=None):
        """
        OWMS-PDA-收货
        :param box: 箱号
        :param sku: 商品编码
        :param c_code: 容器号
        :param r_code: 入库单_单号
        :param header: cookie
        """
        log.info("[ {} ------ confirm_receipt ------ start ]".format(pyname))
        url = host.get("owms_host") + owms_pda_url_sign.get("confirm_receipt", "")
        # 如果外部传入header就更新配置中header的value
        if header:
            login_header['Cookie'] = header
        data = {
            "box": box,
            "sku": sku,
            "type": "munber",
            "munber": 200,
            "container": c_code,
            "receiving_code": r_code,
            "relaType": 1,
            "wa_code_diff_is_ok": 0,
            "now_time": int(time.time()),
            "sku_time": int(time.time()),
            "lc_code": "",
            "wp_code": "",
            "wa_code": ""
        }
        print(data)
        response = requests.post(url=url, headers=login_header, data=data).json()
        print(response)
        assert response.get("status") == 1, response.get("info")
        log.info("[ {} ------ confirm_receipt ------ end ]\n".format(pyname))

    def get_received_log(self, header=None):
        """
        OWMS-PDA-收货验证
        """
        log.info("[ {} ------ get_received_log ------ start ]".format(pyname))
        url = host.get("owms_host") + owms_pda_url_sign.get("confirm_receipt", "")
        # 如果外部传入header就更新配置中header的value
        if header:
            login_header['Cookie'] = header
        print(url)
        response = requests.post(url=url, headers=login_header).json()
        print(response)
        assert response.get("state") == 1, response.get("info")
        log.info("[ {} ------ get_received_log ------ end ]\n".format(pyname))

    def check_container(self, c_code, header=None):
        """
        OWMS-PDA-上架-检查容器
        :param c_code: 容器号
        """
        log.info("[ {} ------ check_container ------ start ]".format(pyname))
        url = host.get("owms_host") + owms_pda_url_sign.get("check_container", "")
        # 如果外部传入header就更新配置中header的value
        if header:
            login_header['Cookie'] = header
        data = { "container": c_code }
        response = requests.post(url=url, headers=login_header, data=data).json()
        print(response)
        assert response.get("status") == 1, response.get("info")
        log.info("[ {} ------ check_container ------ end ]\n".format(pyname))

    def press_sku(self, c_code,sku, header=None):
        """
        OWMS-PDA-上架-检查SKU
        :param c_code: 容器号
        :param sku: 商品编码
        """
        log.info("[ {} ------ press_sku ------ start ]".format(pyname))
        url = host.get("owms_host") + owms_pda_url_sign.get("press_sku", "")
        # 如果外部传入header就更新配置中header的value
        if header:
            login_header['Cookie'] = header
        data = {
            "container": c_code,
            "productBarcode": sku
        }
        response = requests.post(url=url, headers=login_header, data=data).json()
        print(response)
        assert response.get("status") == 1, response.get("info")
        log.info("[ {} ------ press_sku ------ end ]\n".format(pyname))

    def confirm_press(self, c_code,sku, header=None):
        """
        OWMS-PDA-上架
        :param c_code: 容器号
        :param sku: 商品编码
        """
        log.info("[ {} ------ confirm_press ------ start ]".format(pyname))
        url = host.get("owms_host") + owms_pda_url_sign.get("confirm_press", "")
        # 如果外部传入header就更新配置中header的value
        if header:
            login_header['Cookie'] = header
        data = {
            "container": c_code,
            "productBarcode": sku,
            "Press": "LDH-KW3-106",
            "pressMunber": 200
        }
        response = requests.post(url=url, headers=login_header, data=data).json()
        print(response)
        assert response.get("status") == 1, response.get("info")
        log.info("[ {} ------ confirm_press ------ end ]\n".format(pyname))


if __name__ == '__main__':
    from business.login.login_list import project_login