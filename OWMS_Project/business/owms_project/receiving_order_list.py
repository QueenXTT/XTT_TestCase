# -*- Coding: UTF-8 -*-
# Author : Queen_XTT
import requests
from config.url_config import owms_url, host, login_header
from config.parameter_config import owms_project
from common.log import Log
log = Log()
import os
pyname = os.path.basename(__file__)

"""
入库单模块_接口集合
"""
# 获取本业务url和host
owms_url_auth = owms_url.get("receiving", "")

def gcreceiving_sign(receiving_code,header=None):
    """
    查询入库单号
    """
    log.info("[ {} ------ gcreceiving_sign ------ start ]".format(pyname))
    url = host.get("owms_host") + owms_url_auth.get("gcreceiving_sign", "")
    # 如果外部传入header就更新配置中header的value
    if header:
        login_header['Cookie'] = header
    data = {
        "warehouse_code": owms_project.get("warehouse_code"),
        "singleNumber": "receiving_code",
        "singleNumberValue": receiving_code
    }
    response = requests.post(url=url, headers=login_header, data=data).json()
    assert response.get("state") == 1, response.get("message")
    re_data = response.get("data")[0]
    assert re_data.get("receiving_code") == receiving_code, response.get("message")
    box_no = []
    for content in response.get("data"):
        box_no.append(content.get("box_no")) # 获取箱号
    gcreceiving_data = {
        "customer_code": re_data.get("customer_code"), # 获取客户代码
        "box_nos": box_no
    }
    log.info("[ {} ------ gcreceiving_sign ------ end ]\n".format(pyname))
    return gcreceiving_data


if __name__ == '__main__':
    from business.login.login_list import project_login