# -*- coding:utf-8 -*-
# Author:Queen_XTT
from common.log import Log
from business.merchants.merchants_list import Merchants_List
import random

log = Log()
import os

pyname = os.path.basename(__file__)
"""
商户管理_接口组合
"""

merchants_list = Merchants_List()


def random_all_coin(module, token, count=2,mch_user_id=None):
    """
    随机返回_货币类型
    :param count: 随机的数量
    """
    log.info("[ {} ------ random_allcoin ------ start ]".format(pyname))
    new_coin = []
    if mch_user_id != None:
        allcoin = merchants_list.mch_coin_list(module, token,mch_user_id)
    else:
        allcoin = merchants_list.get_allcoin_list(module, token)
    for plist in allcoin:
        if isinstance(plist, str):  # 如果 plist 是字符串类型，直接返回
            plist = allcoin["data"]
            log.info("[ {} ------ random_allcoin ------ end ]".format(pyname))
            return plist
        elif isinstance(plist, dict):  # 如果 plist 是字典类型，直接取值（value）
            for key, value in plist.items():
                if key == "coinName":
                    new_coin.append(value)
    plist = random.sample(new_coin, count)
    log.info("[ {} ------ random_allcoin ------ end ]".format(pyname))
    return plist


def insert_merchants(module, token, m_name, email, role):
    """
    新增商户/搜索商户
    :return:
    """
    log.info("[ {} ------ insert_merchants ------ start ]".format(pyname))
    coin_data = random_all_coin(module, token, 2)
    merchants_data = merchants_list.save_merchant(module, token, m_name, email, coin_data, role)
    merchants_list.get_merchants(module, token, role, m_name, merchants_data["email"])  # 验证新增的商户
    log.info("[ {} ------ insert_merchants ------ end ]".format(pyname))
    return merchants_data


if __name__ == '__main__':
    insert_merchants("admin")
