# -*- coding:utf-8 -*-
# Author:Queen_XTT
from business.login.login_list import user_module_login, getGoogle_code, google_login,query_google_secret_url
from config.url_config import header_config
from common.log import Log
log = Log()
import os
pyname = os.path.basename(__file__)
"""
用户登录_接口组合
"""

header = header_config

def system_login(module, u_name, u_pwd, secret_key=None):
    """
    登录/谷歌验证码
    :param uname: 用户名
    :param upwd: 密码
    :param secretkey: 密钥
    :return: 当前用户的token
    """
    user = user_module_login(module, u_name, u_pwd)
    if user["bindGoogleSecret"]:
        secret_key = query_google_secret_url(module, user["uuid"], user["role"])
    google = getGoogle_code(secret_key)
    login_data = google_login(module, user["uuid"], user["role"], google) # 登录,获取token
    return login_data

if __name__ == '__main__':
    from config.parameter_config import parameter
    from business.module_process.mp_merchant import insert_merchants
    # # system_ligin("Testing", "NfZ1DFvJm/", "OLTOJZLCV6E325OJ")
    # system_login("merchant","zud630@111.com","AnKNQ69wz")
    module = {
        "admin": "admin",
        "merchant": "merchant"
    }
    admin_token = system_login("admin",parameter["user_name"], parameter["user_pwd"],parameter["secret_key"])
    merchants_data = insert_merchants(module["admin"])  # 新增商户/搜索商户
    merchant_token = system_login(module["merchant"], merchants_data["email"],merchants_data["password"])  # 新商户_登录

