# -*- Coding: UTF-8 -*-
# Author : Queen_XTT
import requests
from config.url_config import wms_url, host, login_header
from config.parameter_config import project_name
from common.log import Log
log = Log()
import os
pyname = os.path.basename(__file__)

# 获取本业务url和host
wms_url_auth = wms_url.get("auth", "")

def wms_auth_try(o_id,header=None):
    """
    WMS-执行对应ID的WMS同步队列
    """
    log.info("[ {} ------ wms_auth_try ------ start ]".format(pyname))
    url = host.get("wms_host") + wms_url_auth.get("mq_owms_try", "")
    # 如果外部传入header就更新配置中header的value
    if header:
        login_header['Cookie'] = header
    data = {
        "o_id": o_id,
        "warehouse_code": project_name.get("wms_name")
    }
    response = requests.post(url=url, headers=login_header, data=data).json()
    assert response.get("state") == 1, response.get("message")
    log.info("[ {} ------ wms_auth_try ------ end ]\n".format(pyname))

if __name__ == '__main__':
    from business.login.login_list import project_login
    from business.order.order_list import create_myslq,create_order
    cookies = project_login("wms")
    o_id = create_myslq(create_order())
    code = wms_auth_try(o_id,cookies)