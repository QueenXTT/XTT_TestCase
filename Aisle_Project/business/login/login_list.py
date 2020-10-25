# -*- coding:utf-8 -*-
# Author:Queen_XTT
import requests, base64, time, struct, hmac, hashlib
from config.url_config import header_config, login_url
from common.url_module import query_module_url
from common.log import Log
log = Log()
import os
pyname = os.path.basename(__file__)
"""
用户登录模块
"""
def getGoogle_code(secretkey):
    """
    自动生成_谷歌验证码
    :param secretKey: 账户的_秘钥
    """
    decoded_secretKey = base64.b32decode(secretkey, True)
    interval_number = int(time.time() // 30)
    message = struct.pack(">Q", interval_number)
    digest = hmac.new(decoded_secretKey, message, hashlib.sha1).digest()
    index = ord(chr(digest[19])) % 16
    googleCode = (struct.unpack(">I", digest[index:index+4])[0] & 0x7fffffff) % 1000000
    return "%06d" %googleCode

def user_module_login(module,uname,upwd):
    """
    模块后台_用户登录
    """
    log.info("[ {} ------ user_module_login ------ start ]".format(pyname))
    url = query_module_url(module) + login_url.get("user_login", "")
    data = {"userName":uname,"password":upwd,"locale":"zh"}
    response = requests.post(url=url, headers=header_config, json=data).json()
    assert response.get("msg").lower() == 'success', response.get("msg")
    res = response["data"]
    login_data = {
        "bindGoogleSecret": res["bindGoogleSecret"],
        "role": res["role"],
        "uuid":res["uuid"]
    }
    log.info("[ {} ------ user_module_login ------ end ]\n".format(pyname))
    return login_data

def query_google_secret_url(module,uuid, role):
    """
    查询用户_谷歌密钥
    """
    log.info("[ {} ------ query_google_secret_url ------ start ]".format(pyname))
    url = query_module_url(module) + login_url.get("query_google_url", "")
    data = {"uuid":uuid,"locale":"zh","role":role}
    response = requests.post(url=url, headers=header_config, json=data).json()
    assert response.get("msg").lower() == 'success', response.get("msg")
    google_secret = response["data"]["googleSecret"]
    log.info("[ {} ------ query_google_secret_url ------ end ]\n".format(pyname))
    return google_secret

def google_login(module,uuid,role,secret):
    """
    验证码_登录,获取token
    """
    log.info("[ {} ------ google_login ------ start ]".format(pyname))
    url = query_module_url(module) + login_url.get("google_login", "")
    data = {"uuid":uuid,"secret":secret,"locale":"zh","role":role}
    response = requests.post(url=url, headers=header_config, json=data)
    j_response = response.json()
    assert j_response.get("msg").lower() == '操作成功', j_response.get("msg")
    uheader = response.headers["Set-Cookie"]
    utoken = ""
    for i in uheader.split(";"):
        if i.find("token") != -1:
            utoken = i
    log.info("[ {} ------ google_login ------ end ]\n".format(pyname))
    # print(utoken)
    login = {
        "u_token" : utoken,
        "role" : j_response["data"]["role"]
    }
    return login

if __name__ == '__main__':
    uesr = user_module_login("Testing","NfZ1DFvJm/")
    google = getGoogle_code("OLTOJZLCV6E325OJ")
    utoken = google_login(uesr["uuid"],uesr["role"],google)
    # secret = 'OLTOJZLCV6E325OJ'
    # print(getGoogle_code(secret))