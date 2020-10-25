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
聚合通道页的接口集合
"""

# 获取本业务url和host
url_cluster = admin_url.get("cluster", "")
header = header_config


def query_cluster_list(module, token, role, p_name=None, page=1, size=10):
    """
    聚合通道_初始页
    """
    log.info("[ {} ------ query_cluster_list ------ start ]".format(pyname))
    url = query_module_url(module) + url_cluster.get("query_cluster_list", "")
    data = {"productName": p_name, "pageIndex": page, "pageSize": size, "locale": "zh", "role": role}
    header["cookie"] = token
    response = requests.post(url=url, headers=header, json=data).json()
    assert len(response["data"]["data"]) > 0, "运营后台，聚合通道列表_查询失败\n" + str(response)
    log.info("[ {} ------ query_cluster_list ------ end ]\n".format(pyname))
    return response["data"]


def add_cluster(module, token, role, p_name, preload):
    """
    新增_聚合通道
    :param p_name: 聚合名称
    :param preload: 预加载时间
    :param duration: 统计时长
    :param min_num: 最小单数
    """
    log.info("[ {} ------ add_cluster ------ start ]".format(pyname))
    url = query_module_url(module) + url_cluster.get("add_cluster", "")
    data = {"productName": p_name, "firstRatio": 1, "productCode": "", "preloadInterval": preload,
            "calDuration": preload, "minCardinalNum": preload, "offRate": "0", "locale": "zh", "role": role}
    header["cookie"] = token
    response = requests.post(url=url, headers=header, json=data).json()
    assert response.get('msg').lower() == 'success', response.get('msg')
    log.info("[ {} ------ add_cluster ------ end ]\n".format(pyname))


def edit_cluster(module, token, role, p_name, p_id, code, preload):
    """
    编辑_聚合通道
    """
    log.info("[ {} ------ edit_cluster ------ start ]".format(pyname))
    url = query_module_url(module) + url_cluster.get("edit_cluster", "")
    data = {"productName": p_name, "firstRatio": 1, "productCode": code, "productId": p_id, "preloadInterval": preload,
            "calDuration": preload, "minCardinalNum": preload, "offRate": "0", "locale": "zh", "role": role}
    header["cookie"] = token
    response = requests.post(url=url, headers=header, json=data).json()
    assert response.get('msg').lower() == 'success', response.get('msg')
    log.info("[ {} ------ edit_cluster ------ end ]\n".format(pyname))
