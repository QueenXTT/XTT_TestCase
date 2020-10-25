# -*- Coding: UTF-8 -*-
# Author: Queen_XTT
import requests
from config.url_config import admin_url, header_config
from common.url_module import query_module_url
from common.log import Log

log = Log()
import os

pyname = os.path.basename(__file__)
"""
商户通道页的接口集合
"""
# 获取本业务url和host
url_m_aisle = admin_url.get("merchant_aisle", "")
header = header_config


def query_cluster_combox(module, token, role):
    """
    商户通道_聚合编码数据
    """
    log.info("[ {} ------ query_cluster_combox ------ start ]".format(pyname))
    url = query_module_url(module) + url_m_aisle.get("query_cluster_combox", "")
    data = {"productType": 2, "locale": "zh", "role": role}
    header["cookie"] = token
    response = requests.post(url=url, headers=header, json=data).json()
    assert response.get('msg').lower() == 'success', response.get('msg')
    assert len(response.get("data")) > 0, "运营后台，商户通道_聚合编码接口，没有返回数据\n" + str(response)
    log.info("[ {} ------ query_cluster_combox ------ end ]\n".format(pyname))
    return response.get("data")


def cluster_list(module, token, product_id):
    """
    商户通道_商户数据
    :param product_id: 商户_编号
    """
    log.info("[ {} ------ cluster_list ------ start ]".format(pyname))
    url = query_module_url(module) + url_m_aisle.get("cluster_list", "")
    url_param = {"clusterProductId": product_id}
    header["cookie"] = token
    response = requests.get(url=url, params=url_param, headers=header).json()
    assert response.get('msg').lower() == 'success', response.get('msg')
    assert len(response.get("data")) > 0, "运营后台，商户通道_商户接口，没有返回数据\n" + str(response)
    log.info("[ {} ------ cluster_list ------ end ]\n".format(pyname))
    return response.get("data")


def son_product_list(module, token, role, product_id, mch_user_id):
    """
    商户通道_子通道数据
    """
    log.info("[ {} ------ son_product_list ------ start ]".format(pyname))
    url = query_module_url(module) + url_m_aisle.get("son_product_list", "")
    data = {"clusterProductId": product_id, "mchUserIds": mch_user_id, "locale": "zh", "role": role}
    header["cookie"] = token
    response = requests.post(url=url, headers=header, json=data).json()
    assert response.get('msg').lower() == 'success', response.get('msg')
    assert len(response.get("data")) > 0, "运营后台，商户通道_子通道接口，没有返回数据\n" + str(response)
    log.info("[ {} ------ son_product_list ------ end ]\n".format(pyname))
    return response.get("data")


def batch_merchant_config(module, token, role, product_id, mch_list, product_list ):
    """
    配置_商户通道操作
    """
    log.info("[ {} ------ batch_merchant_config ------ start ]".format(pyname))
    url = query_module_url(module) + url_m_aisle.get("batch_merchant_config", "")
    data = {"clusterProductId": product_id, "mchList": mch_list, "productList": product_list, "locale": "zh",
            "role": role}
    header["cookie"] = token
    response = requests.post(url=url, headers=header, json=data).json()
    assert response.get('msg').lower() == 'success', response.get('msg')
    log.info("[ {} ------ batch_merchant_config ------ end ]\n".format(pyname))
