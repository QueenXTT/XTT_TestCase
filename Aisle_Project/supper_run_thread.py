# -*- coding:utf-8 -*-
# Author:Queen_XTT

import os
import time
import unittest
from common import HTMLTestRunner_cn_supper
from common.get_data_common import Get_Data
from BeautifulReport import BeautifulReport
from tomorrow import threads


class RunMain():
    thread_num = 10  # 多线程线程数

    def __init__(self):
        self.get_d = Get_Data()
        self.report_file = 'test_business/report'  # 报告路径
        self.case_file = 'test_business'  # case路径

        self.now = time.strftime("%Y_%m_%d %H_%M_%S")
        cur_path = os.path.dirname(os.path.realpath(__file__))  # 获取当前脚本所在真实路径
        self.report_path = os.path.join(cur_path, self.report_file)  # 报告路径
        if not os.path.exists(self.report_path):
            os.mkdir(self.report_path)  # 如果不存在报告路径下report文件夹，则自动创建
        self.report_abspath = os.path.join(
            self.report_path, self.now + "_result.html")  # 拼接html报告名称、时间、路径

    def run_case(self):
        """
        加载case--运行case--生成报告
        """
        # 加载self.case_file文件夹下，以test*.py开头的unittest用例
        discover = unittest.defaultTestLoader.discover(
            self.case_file, "test*.py")
        # 报告配置
        run = HTMLTestRunner_cn_supper.HTMLTestRunner(title="接口自动化业务流测试报告",
                                                      description="windows10 ,requests",
                                                      stream=open(
                                                          self.report_abspath, "wb"),
                                                      retry=0)  # 失败重试次数
        run.run(discover)  # 运行加载的用例
        print("------run case finish !------")

    # 多线程运行

    def thread_run_case(self):
        """
        加载case和运行多线程主方法
        :param case_path: casa路径
        """
        discover = unittest.defaultTestLoader.discover(self.case_file, pattern='test*.py',
                                                       top_level_dir=None)  # 加载路径下所有case
        for i in discover:
            self.__run(i)  # 多线程运行case

    @threads(thread_num)  # 线程装饰器，the_num为当前线程数
    def __run(self, discover):
        """
        运行case，生成多线程报告
        :param discover: case
        """
        # 使用BeautifulReport去跑case并生产报告
        result = BeautifulReport(discover)
        result.report(filename=os.path.join(self.now + '_thread_report.html'), description='多线程接口自动化测试报告',
                      log_path=self.report_path)


if __name__ == "__main__":
    run = RunMain()
    # run.run_case()  # 运行case
    #
    run.thread_run_case()  # 多线程运行case
