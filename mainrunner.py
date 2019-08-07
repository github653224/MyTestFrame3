# coding:utf8
from common.Excel import *
from interface.inter import *
import inspect

"""
    这是整个自动化框架的主代码运行入口
    powered by will
    at: 2019/08/05
"""


def runcase(line, f):
    # # 使用条件语句，判断字符串，然后调用指定方法
    # if line[3] == 'post':
    #     http.post(line[4],line[5],line[6])
    #     return
    #
    # if line[3] == 'assertequals':
    #     http.assertequals(line[4],line[5])
    #     return

    # 分组信息，不用执行
    if len(line[0]) > 0 or len(line[1]) > 0:
        return

    # 反射获取关键字函数
    func = getattr(f, line[3])
    # 获取参数列表
    args = inspect.getfullargspec(func).__str__()
    args = args[args.find('args=') + 5:args.rfind(', varargs')]
    args = eval(args)
    args.remove('self')
    # 不接收参数的调用
    if len(args)==0:
        func()
        return

    if len(args)==1:
        func(line[4])
        return

    if len(args)==2:
        func(line[4],line[5])
        return

    if len(args)==3:
        func(line[4],line[5],line[6])
        return

    print('warning：目前只支持3个参数的关键字')


# 接口自动化运行
reader = Reader()
reader.open_excel('./lib/HTTP接口用例.xls')
sheetname = reader.get_sheets()

writer = Writer()
writer.copy_open('./lib/HTTP接口用例.xls', './lib/result-HTTP接口用例.xls')
http = HTTP(writer)

for sheet in sheetname:
    # 设置当前读取的sheet页面
    reader.set_sheet(sheet)
    # 保持读写在同一个sheet页面
    writer.set_sheet(sheet)
    for i in range(reader.rows):
        writer.row = i
        line = reader.readline()
        runcase(line, http)

writer.save_close()