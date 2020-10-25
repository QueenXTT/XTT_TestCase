# -*- Coding: UTF-8 -*-
# Author  : Queen_XTT

import unittest,time,os
from common import HTMLTestRunner_cn_supper

"""
加载和运行unittest，并生成html测试报告
"""


def run_case():
    now = time.strftime("%Y_%m_%d %H_%M_%S")
    cur_path = os.path.dirname(os.path.realpath(__file__))  # 获取当前脚本所在真实路径
    report_path = os.path.join(cur_path, "report")  # 报告路径
    if not os.path.exists(report_path):
        os.mkdir(report_path)  # 如果不存在报告路径下report文件夹，则自动创建
    report_abspath = os.path.join(
        report_path, now + "result.html")  # 拼接html报告名称、时间、路径

    if __name__ == "__main__":
        discover = unittest.defaultTestLoader.discover(
            "test_case", "test*.py")  # 加载testcase文件夹下，以test*.py开头的，unittest用例
        # 报告配置
        run = HTMLTestRunner_cn_supper.HTMLTestRunner(title="Python_接口自动化测试报告",
                                                      description="windows10 ,requests",
                                                      stream=open(
                                                          report_abspath, "wb"),
                                                      retry=0)  # 失败重试次数
        run.run(discover)  # 运行加载的discover用例

    print("------ run case finish ! ------")


if __name__ == "__main__":
    run_case()  # 运行
