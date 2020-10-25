# -*- coding:utf-8 -*-
# Author:Queen_XTT
from config.url_config import host, module_url

"""
URL_模块区分
"""


def query_module_url(module):
    """
    获取系统模块_拼接URL
    :param modile:
    :return:
    """
    system_host = host.get("host", "")
    if module == "admin":
        system_host += module_url.get("admin", "")
    elif module == "merchant":
        system_host += module_url.get("merchant", "")
    # print(system_host)
    return system_host


def request_page(total_count, page_size):
    """
    获取_请求页码
    :param total_count: 总计
    :param page_size: 每页显示数量
    :return: 总页数
    """
    total = total_count / page_size
    if total_count % page_size == 0:
        page = total
    else:
        count = str(total).split(".")[0]
        page = int(count) + 1
    return int(page)


if __name__ == '__main__':
    query_module_url("merchant")
