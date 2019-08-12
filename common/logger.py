# coding:utf8
import logging

"""
        powered by Mr Will
           at 2018-12-22
        用来格式化打印日志到文件和控制台
"""
path = '.'
logger = None
# create logger
# 这里可以修改开源模块的日志等级
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
c = logging.FileHandler(path + "/lib/all.log", mode='a', encoding='utf8')
logger = logging.getLogger('frame log')
logger.setLevel(logging.DEBUG)
c.setFormatter(formatter)
logger.addHandler(c)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# # add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)


# 打印debug级别日志
def debug(ss):
    global logger
    try:
        logger.debug(str(ss))
    except:
        return


# 打印info级别日志
def info(ss):
    global logger
    try:
        logger.info(str(ss))
    except:
        return


# 打印debug级别日志
def warn(ss):
    global logger
    try:
        logger.warning(str(ss))
    except:
        return


# 打印error级别日志
def error(ss):
    global logger
    try:
        logger.error(str(ss))
    except:
        return


# 打印异常日志
def exception(e):
    global logger
    try:
        logger.exception(e)
    except:
        return


# 调试
if __name__ == '__main__':
    debug('test')
    error('error')
    warn('warnning')
    try:
        a = 1
        print(a + '1')
    except Exception as e:
        exception(e)
