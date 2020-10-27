# -*- Coding: UTF-8 -*-
# Author : Queen_XTT

header_config = {
    "Content-Type": "application/json; charset=utf-8"
}
login_header = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}
"""
URL：管理集合
"""

host = {
    "oms_host": "https://test-oms.eminxing.com",
    "wms_host": "http://test-wms.eminxing.com",
    "owms_host": "http://test-owms-usea.eminxing.com"
}

# 【系统登录】
login_url = {
    "login": "/login.html", # 【OMS，OWMS】登录
    "omws_pda_login": "/pda/login/login" # OWMS_PDA_登录
}

# 【OMS_系统】
oms_url = {
    # 订单功能
    "order": {
        "web_service": "/default/svc/web-service" # 新增订单数据
    }
}
# 【WMS_系统】
wms_url = {
    # 验证
    "auth": {
        "mq_owms_try": "/auth/mq-owms/try" # WMS-执行对应ID的WMS同步队列
    }
}
# 【OWMS_系统】
owms_url = {
    # 入库单模块
    "receiving": {
        "gcreceiving_sign": "/gcreceiving/sign/list" # 查询入库单号
    },
    # 容器模块
    "container": {
        "container_create": "/container/container/create"  # 查询入库单号
    },
    # 批次日志模块
    "batch_log": {
        "inventory_batch_log": "/warehouse/inventory-batch-log/list" # 批次日志_查询
    },
}

# 【OWMS_PDA_系统】
owms_pda_url = {
    # 入库单_签收_模块
    "order_shelves": {
        "press_box_sign": "/pda/gc-receiving/press-box-sign", # 按箱签收_签收
        "validate_box": "/pda/gc-receiving/validate-box", # 收货_箱号/SKU_验证
        "get_sku_inventory": "/pda/gc-receiving/get-sku-inventory", # 收货_获取SKU库存
        "confirm_receipt": "/pda/gc-receiving/confirm-receipt", # 收货
        "get_received_log": "/pda/gc-receiving/get-received-log", # 收货验证
        "check_container": "/pda/gc-putaway/check-container", # 上架_检查容器
        "press_sku": "/pda/gc-putaway/press-sku", # 上架_检查SKU
        "confirm_press": "/pda/gc-receiving/confirm-press", # 上架
        "batch_sign": "/pda/gc-receiving/batch-sign" # 批量签收_签收
    }
}

if __name__ == '__main__':
    print(header_config["Content-Type"])
    # order_url = admin_url["order"]
    # print(order_url.get("create_order"))
