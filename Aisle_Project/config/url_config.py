# -*- coding:utf-8 -*-
# Author:Queen_XTT

"""
URL：管理集合
"""

host = {
    "host": "https://f2.entry.one"
}

header_config = {
    "Content-Type": "application/json;charset=UTF-8",
    "ffbodysign": "841288841d59b88ec16f281d01c2bbf933b42d7a83aeca8f44a0dd2713c6f923"
}

# 【项目模块分类】
module_url = {
    "admin": "/manage/admin",  # 运营后台
    "merchant": "/manage/merchant"  # 商户后台
}

# 登录功能
login_url = {
    "user_login": "/login",  # 运营后台_登录
    "query_google_url": "/queryUserGoogleSecretUrl",  # 查询用户_谷歌密钥
    "google_login": "/googleCodeVerify"  # 谷歌验证码_登录
}
# 【运营系统后台】
admin_url = {
    # 订单功能
    "order": {
        "create_order": "/soapi/pay/unifiedorder", # 新增订单数据
        "order_list": "/orderList",
        "order_info": "/orderDetailByOutTradeNo"
    },
    # 商户模块
    "merchants": {
        "merchant_app_list": "/appList",  # 商户API_列表
        "allcoin_list": "/allCoinList?locale=zh",  # 货币类型
        "save_merchant": "/saveMerchant",  # 新增_商户
        "merchant_List": "/merchantList",  # 商户_列表
        "add_app": "/addApp",  # 新增_商户应用
        "app_list": "/appList",  # 商户应用_初始页
        "save_Merchant": "/saveMerchant",  # 编辑_商户应用
        "op_merchant": "/opMerchant?s&s&locale=zh",  # 启用/禁用_商户状态
        "reset_merchant_pwd": "/resetMerchantLoginPwd?s&locale=zh",  # 重置商户密码
        "reset_merchant_google": "/restMerchantGoogleSecret",  # 重置商户_谷歌验证码
        "op_app": "/opApp?s&s&locale=zh",  # 启用/禁用_商户APP状态
        "update_app": "/adminUpdateApp",  # 编辑商户APP白名单
        "mch_combo_list": "/mchComboList?locale=zh",  # API_商户名称
        "mch_coin_list": "/merCoinList?s&locale=zh"  # API_商户名称
    },
    # 聚合通道
    "cluster": {
        "query_cluster_list": "/queryClusterProductList",  # 聚合通道_列表
        "add_cluster": "/addClusterProduct",  # 新增_聚合通道
        "edit_cluster": "/editClusterProduct",  # 编辑_聚合通道
    },
    # 通道（子通道）
    "aisle": {
        "aisle_list": "/aisleTypeList",  # 通道_列表
        "aisle_combo": "/aisleCombo?locale=zh",  # 通道供应商_下拉框数据
        "delivery_product": "/queryDeliveryUserCombox",  # 通道_下发人
        "op_aisle_type": "/opAisleType?s&s&locale=zh", # 启用/禁用_通道状态
        "save_aisle_type": "/saveAisleType", # 编辑_通道数据
        "query_assurer_combox": "/queryMemberAssurerCombox?locale=zh", # 查询_成员组合
        "pay_product_list": "/payProductList", # 查询_成员组合
        "aisle_order": "/aisleOrder", # 通道_订单测试
        "aisle_channel": "/aisleChannel?s&locale=zh", # 通道_订单测试
        "save_product": "/savePayProduct", # 通道_订单测试
        "up_product_credit": "/modifyPayProductCredit", # 通道_订单测试
        "op_pay_product": "/opPayProduct?s&s&locale=zh", # 启用/禁用_子通道状态
    },
    # 商户通道配置
    "merchant_aisle": {
        "query_cluster_combox": "/queryClusterPayProductCombox",  # 聚合编码_数据
        "cluster_list": "/clusterMchList?s&locale=zh",  # 商户通道_商户数据
        "son_product_list": "/sonPayProductList",  # 商户通道_子通道数据
        "batch_merchant_config": "/batchSaveMchConfig",  # 商户通道_子通道数据
    },
}

# 【商户系统后台】
merchant_url = {

}

if __name__ == '__main__':
    # print(memer_url["member-list"])
    # order_url = admin_url["order"]
    # print(order_url.get("create_order"))
    print(module_url.get("admin").split("/")[-1])
