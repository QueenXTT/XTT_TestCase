# -*- coding:utf-8 -*-
# Author:Queen_XTT
import os

# 格式化字符串的函数；语法是通过 {} 和 : 来代替以前的 % ；比+号拼接效率高
''' format() '''

# 检查你输入的是否是字符类型
''' isinstance() '''

# 检测字符串是否只由数字组成
''' isdigit() '''

# 对字符串进行分隔，转化为：列表
''' split() '''

# 把字符串 old（旧字符串）替换成 new (新字符串)
''' replace() '''

#（元组、列表、字典、字符串) 转化为：字符串
''' join() '''

# 遍历（列表、元组或字符串），列出数据和数据下标
''' enumerate() '''

# 代码执行完毕，关闭打开的文件
''' with '''

# 在【列表】末尾添加新的对象
''' append() '''

# 检查字符串是否是以指定子字符串开头
''' startswith() '''

' python去掉字符串中空格的方法 '

# 把头和尾的空格去掉
''' strip() '''

# 把左边的空格去掉
''' lstrip() '''

# 把右边的空格去掉
''' rstrip() '''

# 把字符串里的c1替换成c2，可以用replace(' ','')来去掉字符串里的所有空格
''' replace('c1','c2')  '''

# 通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
''' split() '''


' 调用上级目录的同级的子文件方法 '

# 当前程序的【相对路径】
''' __file__ '''

' 动态的获取程序的绝对路径，加到环境变量里，方便别人调用程序 '
import os,sys  # 引用 os 模块

os.path.abspath(__file__)  # 当前程序的【绝对路径】

os.path.dirname()  # 返回目录名，不要文件名

os.path.dirname( os.path.dirname() )  # 获取程序的父级的【绝对路径】

CretidCard = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 获取上两级的【绝对路径】

sys.path.append(CretidCard)  # 添加环境变量