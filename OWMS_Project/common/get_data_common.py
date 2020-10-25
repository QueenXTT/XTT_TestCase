# -*- Coding: UTF-8 -*-
# Author : Queen_XTT
import json
#import xlrd
from common.log import Log
log = Log()
import os
pyname = os.path.basename(__file__)
"""
读取文件的公共方法
"""
class Get_Data():


    def assert_repose(self,expect, response,error_msg='None'):
        """校验接口返回值"""
        assert expect in str(response), '断言失败: ' + str(error_msg)

    def write_data(self, data, filename=None):
        """写数据"""
        filename = './login_token.txt' if not filename else filename
        with open(filename, 'w+') as fp:
            return fp.write(json.dumps(data))


    def read_data(self, filename=None):
        """获取数据"""
        filename = './login_token.txt' if not filename else filename
        with open(filename, 'r+') as fp:
            return json.loads(fp.read())


    def get_data_file(self,module,filename):
        '''自动获取项目测试数据的路径'''
        file = os.path.dirname(__file__) # 获取文件路径
        project_dir = os.path.dirname(file) #获取项目路径
        file_name = os.path.join(project_dir,module,filename)
        return file_name

    def load_xml(self,module,filename):
        '''读取 xml 文件数据'''
        file = self.get_data_file(module,filename)
        with open(file,"r",encoding="UTF-8") as dt:
            data = dt.read()
        return data
    #
    # def get_excel_data(self,filename, api_name=None):
    #     '''读取 excel 文件数据'''
    #     book = xlrd.open_workbook(filename) # 打开Excel文件读取数据
    #     table = book.sheet_by_index(0) # 通过索引顺序获取
    #     data = []
    #     for row in range(1,table.nrows): # 从表格的第二行开始读取
    #         data.append(list(table.row_values(row,0,table.ncols))) # 从表格的第1列开始读取
    #     if api_name: # 在 api_name 不为空，返回 api_name 对应的数据list
    #         data_list = [i for i in data if api_name in i]
    #         return data_list
    #     return data

    def setup_login_config(self,index,username):
        '''更新 login_config 文件的参数'''
        log.info("[ {} ------ setup_login_config ------ start ]".format(pyname))
        txt = self.get_data_file("common/login_setup", "login_config.txt")
        with open(txt,"r",encoding="UTF-8") as tr: # 以只读的方式打开文件
            values = tr.read().split(",") # 将txt的内容按 ，进行分隔，转化为：列表
            values[index] = username # 更改第 index 参数

        with open(txt, "w", encoding="UTF-8") as tw: # 用于写入，即原有内容会被删除
            for content in range(0,len(values)): # 依次将列表的值写入
                tw.write(values[content])
                if (content+1) < len(values): # 除最后一个值
                    tw.write(",") # 以逗号拼接
        log.info("[ {} ------ setup_login_config ------ end ]\n".format(pyname))



if __name__ == '__main__':
    getdata = Get_Data()
    # getdata.load_yaml(
    # filename = './login_token.txt'
    # with open(filename)as fp:
    #     print(fp.read())
    res = {'code': 62005, 'msg': '用户未登录', 'data': None, 'errBody': None}
    ex = "'data': None"
    getdata.assert_repose(ex, res)
    getdata.load_xml()


