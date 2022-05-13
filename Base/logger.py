# -*- coding: utf-8 -*-
# @File    : logger.py
import logging
import os.path
import time
from logging.handlers import TimedRotatingFileHandler

class Logger(object):
    def __init__(self,logger):
        # 获取项目路径，避免路径丢失的情况
        self.project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        # 格式化当前时间:
        self.rq = time.strftime('%Y_%m_%d_%H_%M', time.localtime(time.time()))
        # 配置日志路径
        self.log_path = self.project_path + '/log/'
        # 日志每天的内容保存在一个文件中
        self.log_rq = time.strftime('%Y%m%d', time.localtime(time.time()))
        # 日志的名称：
        self.log_name = self.log_path + self.log_rq + '.log'
        # 日志的输入格式
        self.log_formate = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

        '''
        指定保存日志的文件路径、日志级别、以及调用文件，将日志写入到指定的文件中
        :param logger:
        '''
        #创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        #创建一个handler,用于写入到log 文件中
        fh = logging.FileHandler(self.log_name)
        fh.setLevel(logging.INFO)

        #在创建一个handler,用于输入到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        #定义handler的输出格式
        formatter = logging.Formatter(self.log_formate)
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

