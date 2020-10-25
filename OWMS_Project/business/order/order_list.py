# -*- Coding: UTF-8 -*-
# Author : Queen_XTT

import requests
from config.url_config import oms_url, host, header_config
from common.log import Log
from common.get_data_common import Get_Data
log = Log()
import os,re,time
get_data = Get_Data()
import pymysql
pyname = os.path.basename(__file__)

"""
订单模块的接口集合
"""
# 获取本业务url和host
oms_url_order = oms_url.get("order", "")
header = header_config


# host = host.get("host", "") + module_url.get("admin", "")
# url_order = admin_url.get("order", "")


def create_order():
    """
    创建并审核入库单-自发-标准-快递
    """
    log.info("[ {} ------ create_order ------ start ]".format(pyname))
    url = host.get("oms_host") + oms_url_order.get("web_service", "")
    body = get_data.load_xml("xml_data/oms","oms_receiving_order.xml") # 调用 xml_data\oms 目录的 新增入库单 XML
    response = requests.post(url, data=body.encode("utf-8"), headers=header, verify=False)
    assert response.status_code == 200, "OMS - 创建入库单失败\n"+response.text
    log.info("[ {} ------ create_order ------ end ]".format(pyname))
    receiving_code = ''.join(re.findall(r'"receiving_code":"(.+?)"}}', response.text)) # 正则获取入库单号，转成 str 格式
    return receiving_code


def create_myslq(receiving_code):
    """
    链接数据库，执行SQL
    :param receiving_code: 入库单_单号
    """
    db = pymysql.connect(
         host="192.168.109.239",    # 服务器地址
         port=63308, # 端口号
         user="goodcang_test",         # 用户名
         passwd="O0M8HaQJnpWCyIYa",  # 密码
         db="goodcang_wms_test",        # 数据库名称
         charset = 'utf8')

    cur = db.cursor() # 查询前，必须先获取游标
    cur.execute(r"SELECT o_id FROM `mq_owms` WHERE body LIKE '%%%s%%'" % receiving_code) # 执行的都是原生SQL语句
    sql_data = cur.fetchall()
    o_id = 0
    for row in sql_data:
        o_id = row[0]
    db.close()
    # print(o_id
    time.sleep(3)
    return o_id


if __name__ == '__main__':

    code = create_order()
    create_myslq(code)
