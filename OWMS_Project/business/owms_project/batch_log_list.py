# -*- Coding: UTF-8 -*-
# Author : Queen_XTT
import requests
from config.url_config import owms_url, host, login_header
from common.log import Log
log = Log()
import os
pyname = os.path.basename(__file__)

"""
批次日志模块_接口集合
"""
# 获取本业务url和host
owms_url_batch = owms_url.get("batch_log", "")

def inventory_batch_log(r_code, header=None):
    """
    OWMS-美东-批次日志-查询
    :param receiving_code: 入库单_单号
    :param sku: 商品编码
    """
    log.info("[ {} ------ inventory_batch_log ------ start ]".format(pyname))
    url = host.get("owms_host") + owms_url_batch.get("inventory_batch_log", "")
    # 如果外部传入header就更新配置中header的value
    if header:
        login_header['Cookie'] = header
    data = { "receiving_code": r_code }
    response = requests.post(url=url, headers=login_header, data=data).json()
    assert response.get("state") == 1, response.get("info")
    print(response)
    log.info("[ {} ------ inventory_batch_log ------ end ]\n".format(pyname))


if __name__ == '__main__':
    from business.login.login_list import project_login