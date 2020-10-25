# -*- Coding: UTF-8 -*-
# Author : Queen_XTT

import requests
from config.url_config import login_url, host, login_header
from config.parameter_config import project_name,login_account
from common.log import Log
log = Log()
import os,re
pyname = os.path.basename(__file__)

"""
各系统登录接口集合
"""
# 获取本业务url和host
logins_url = login_url.get("order", "")

def project_login(module):
    """
    系统后台_用户登录
    """
    log.info("[ {} ------ project_login ------ start ]".format(pyname))
    url = data = ""
    if module == project_name.get("wms_name"):
        url = host.get("wms_host") + login_url.get("login", "")
        data = {"userName": login_account.get("login_name"), "userPass": login_account.get("login_pwd")}
    elif module == project_name.get("owms_name"):
        url = host.get("owms_host") + login_url.get("login", "")
        data = {"userName": login_account.get("login_name"), "userPass": login_account.get("login_pwd")}
    elif module == project_name.get("owms_pda_name"):
        url = host.get("owms_host") + login_url.get("omws_pda_login", "")
        data = {"user": login_account.get("login_name"), "pass": login_account.get("login_pwd")}
    response = requests.post(url=url, headers=login_header, data=data)
    if module == project_name.get("owms_pda_name"):
        assert response.json().get("status") == 1, response.json().get("message")
    else:
        assert response.json().get("state") == 1, response.json().get("message")
    PHPSESSID = "PHPSESSID={}".format("".join(re.findall(r"PHPSESSID=(.+?);",response.headers.get("Set-Cookie"))))# 获取headers中的PHPSESSID)
    log.info("[ {} ------ project_login ------ end ]\n".format(pyname))
    return PHPSESSID

if __name__ == '__main__':

    code = project_login("wms")