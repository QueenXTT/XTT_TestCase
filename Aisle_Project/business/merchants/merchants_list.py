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
商户模块的接口集合
"""

# 获取本业务url和host
url_merchants = admin_url.get("merchants", "")
header = header_config


class Merchants_List():

    def get_merchants_appid(self, module, token, role, mch_user_id=None, appname=None, ip=None, page=1):
        """
        商户API_初始页
        """
        log.info("[ {} ------ get_merchants_appid ------ start ]".format(pyname))
        url = query_module_url(module) + url_merchants.get("merchant_app_list", "")
        data = {"mchUserId": mch_user_id, "appName": appname, "pageIndex": page, "pageSize": 10, "locale": "zh",
                "ip": ip, "role": role}
        header["cookie"] = token
        response = requests.post(url=url, headers=header, json=data).json()
        assert response.get('msg').lower() == '操作成功', response.get('msg')
        # res = response["data"]["data"][0]
        # merchant = {
        #     "appId": res["appId"],
        #     "userId": res["userId"]
        # }
        log.info("[ {} ------ gest_merchants_appid ------ end ]\n".format(pyname))
        return response["data"]

    def get_allcoin_list(self, module, token):
        """
        货币_类型
        """
        log.info("[ {} ------ get_allcoin_list ------ start ]".format(pyname))
        url = query_module_url(module) + url_merchants.get("allcoin_list", "")
        header["cookie"] = token
        response = requests.get(url=url, headers=header).json()
        assert response.get('msg').lower() == '操作成功', response.get('msg')
        log.info("[ {} ------ get_allcoin_list ------ end ]".format(pyname))
        return response.get('data')

    def save_merchant(self, module, token, m_name, email, coin, role, user_id=None, m_id=None, float_amount=None):
        """
        新增/编辑_商户数据
        :param module: 系统模块
        :param token: cookie
        :param m_name: 商户名称
        :param email: 商户账号
        :param coin: 货币类型
        :param role: 角色
        :param user_id: 用户编号
        :param m_id: 商户编号
        :param float_amount: 下浮金额
        """
        log.info("[ {} ------ save_Merchant ------ start ]".format(pyname))
        url = query_module_url(module) + url_merchants.get("save_Merchant", "")
        data = {"userId": user_id, "merchantId": m_id, "floatDownAmount": float_amount, "companyName": m_name,
                "email": email, "supportCoinList": coin, "locale": "zh", "role": role}
        header["cookie"] = token
        response = requests.post(url=url, headers=header, json=data).json()
        assert response.get('msg').lower() == '操作成功', response.get('msg')
        log.info("[ {} ------ save_Merchant ------ end ]\n".format(pyname))

    def get_merchants(self, module, token, role, merchantname=None, account=None, page=1):
        """
        商户_初始页
        """
        log.info("[ {} ------ get_merchants ------ start ]".format(pyname))
        url = query_module_url(module) + url_merchants.get("merchant_List", "")
        data = {"merchantName": merchantname, "merchantAccount": account, "pageIndex": page, "pageSize": 10,
                "locale": "zh",
                "role": role}
        header["cookie"] = token
        response = requests.post(url=url, headers=header, json=data).json()
        assert response["data"].get('totalCount') > 0, response.get('msg')
        log.info("[ {} ------ get_merchants ------ end ]\n".format(pyname))
        return response


    def save_merchant_app(self, module, token, role, mch_user_id, app_name, api_domain, coin_list, white_list=None):
        """
        新增_商户应用
        :param mch_user_id: 商户编号
        :param app_name: 应用名称
        :param api_domain: 访问域名
        :param coin_list: 支持的币种
        :param white_list: IP白名单
        """
        log.info("[ {} ------ save_merchant ------ start ]".format(pyname))
        url = query_module_url(module) + url_merchants.get("add_app", "")
        data = {"mchUserId": mch_user_id, "apiDomain": api_domain, "frontDomain": api_domain, "appName": app_name,
                "appType": 1, "status": 1, "supportCoinList": coin_list, "whiteList": white_list, "locale": "zh",
                "role": role}
        header["cookie"] = token
        response = requests.post(url=url, headers=header, json=data).json()
        assert response.get('msg').lower() == '操作成功', response.get('msg')
        log.info("[ {} ------ save_merchant ------ end ]\n".format(pyname))

    def op_merchant(self, module, token, op_type, user_id):
        """
        启用/禁用_商户状态
        :param op_type: 商户_状态
        :param user_id: 用户_编号
        """
        log.info("[ {} ------ op_merchant ------ start ]".format(pyname))
        url = query_module_url(module) + url_merchants.get("op_merchant", "")
        url_param = {"opType": op_type, "userId": user_id}
        header["cookie"] = token
        response = requests.get(url=url, params=url_param, headers=header).json()
        assert response.get('msg').lower() == '操作成功', response.get('msg')
        log.info("[ {} ------ op_merchant ------ end ]\n".format(pyname))

    def reset_merchant_pwd(self, module, token, user_id):
        """
        重置_商户密码
        :param user_id: 用户_编号
        """
        log.info("[ {} ------ reset_merchant_pwd ------ start ]".format(pyname))
        url = query_module_url(module) + url_merchants.get("reset_merchant_pwd", "")
        url_param = {"userId": user_id}
        header["cookie"] = token
        response = requests.get(url=url, params=url_param, headers=header).json()
        assert response.get('msg').lower() == '操作成功', response.get('msg')
        log.info("[ {} ------ reset_merchant_pwd ------ end ]\n".format(pyname))
        return response.get("data")

    def reset_merchant_google(self, module, token, user_id, role):
        """
        重置_google_验证码
        :param user_id: 用户_编号
        """
        log.info("[ {} ------ reset_merchant_google ------ start ]".format(pyname))
        url = query_module_url(module) + url_merchants.get("reset_merchant_google", "")
        data = {"restUserId": user_id, "locale": "zh", "role": role}
        header["cookie"] = token
        response = requests.post(url=url, headers=header, json=data).json()
        assert response.get('msg').lower() == 'success', response.get('msg')
        log.info("[ {} ------ reset_merchant_google ------ end ]\n".format(pyname))

    def op_app(self, module, token, app_id, op_type):
        """
        启用/禁用_API列表状态
        """
        log.info("[ {} ------ op_app ------ start ]".format(pyname))
        url = query_module_url(module) + url_merchants.get("op_app", "")
        url_param = {"appId": app_id, "opType": op_type}
        header["cookie"] = token
        response = requests.get(url=url, params=url_param, headers=header).json()
        assert response.get('msg').lower() == '操作成功', response.get('msg')
        log.info("[ {} ------ op_app ------ end ]\n".format(pyname))

    def update_app(self, module, token, app_id, white, role):
        """
        编辑商户APP白名单
        :param module: 系统模块
        :param token: cookie
        :param app_id: APP编号
        :param white: 白名单
        :param role: 角色
        """
        log.info("[ {} ------ update_app ------ start ]".format(pyname))
        url = query_module_url(module) + url_merchants.get("update_app", "")
        data = {"appId": app_id, "whiteList": white, "role": role, "locale": "zh"}
        header["cookie"] = token
        response = requests.post(url=url, headers=header, json=data).json()
        assert response.get('msg').lower() == '操作成功', response.get('msg')
        log.info("[ {} ------ update_app ------ end ]\n".format(pyname))
        return response["data"]

    def mch_combo_list(self, module, token):
        """
        API_商户名称下拉框数据
        """
        log.info("[ {} ------ mch_combo_list ------ start ]".format(pyname))
        url = query_module_url(module) + url_merchants.get("mch_combo_list", "")
        header["cookie"] = token
        response = requests.get(url=url, headers=header).json()
        assert response.get('msg').lower() == '操作成功', response.get('msg')
        log.info("[ {} ------ mch_combo_list ------ end ]\n".format(pyname))
        return response.get("data")

    def mch_coin_list(self, module, token, mch_user_id):
        """
        商户对应的_支持币种
        """
        log.info("[ {} ------ mch_coin_list ------ start ]".format(pyname))
        url = query_module_url(module) + url_merchants.get("mch_coin_list", "")
        url_param = {"mchUserId": mch_user_id}
        header["cookie"] = token
        response = requests.get(url=url, params=url_param, headers=header).json()
        assert response.get('msg').lower() == '操作成功', response.get('msg')
        log.info("[ {} ------ mch_coin_list ------ end ]\n".format(pyname))
        return response.get("data")

if __name__ == '__main__':
    # res = get_merchants_appid("pdx-cs123")
    # print(res)
    # res = get_allcoin_list()
    # print(res)
    sss = {'code': 0, 'msg': '操作成功', 'data': {'pageIndex': 1, 'pageSize': 10, 'totalCount': 24, 'data': []},
           'errBody': None}
    print(len(sss["data"]["data"]))
    assert len(sss["data"]["data"]) > 0, "运营后台，API列表_查询失败"
