# -*- Coding: UTF-8 -*-
# Author : Queen_XTT
import requests
from config.url_config import owms_url, host, login_header
from common.log import Log
log = Log()
import os
pyname = os.path.basename(__file__)

"""
【容器】模块_接口集合
"""
# 获取本业务url和host
owms_url_container = owms_url.get("container", "")

def container_create(header=None):
    """
    OWMS-美东-创建拣货容器
    """
    log.info("[ {} ------ container_create ------ start ]".format(pyname))
    url = host.get("owms_host") + owms_url_container.get("container_create", "")
    # 如果外部传入header就更新配置中header的value
    if header:
        login_header['Cookie'] = header
    data = {
        "add_c_name": "xtt_001",
        "add_c_status": 2,
        "add_c_work_code": "XTT000",
        "add_ct_id": 6,
        "add_ctt_modes": 1,
        "add_wp_code": "USEA—A",
        "warehouse_id": 1
    }
    response = requests.post(url=url, headers=login_header, data=data).json()
    assert response.get("state") == 1, response.get("message")
    log.info("[ {} ------ container_create ------ end ]\n".format(pyname))
    return response.get("code")

if __name__ == '__main__':
    from business.login.login_list import project_login