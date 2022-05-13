# -*- coding: utf-8 -*-
# @File    : deletebot.py
import json

from Base.logger import Logger
from Base.request_method import RequestMethod
from Config.request_data import RequestData
from Config.request_url import ReqeustUrl
from Config.request_header import RequestHeader


class DeleteBot(object):
    def __init__(self):
        self.appid = RequestData.appid
        self.header = RequestHeader.header
        self.request_data = RequestData.delete_bot_data
        url = ReqeustUrl.deletebot_url
        self.new_url = url + self.appid + '?reason=undefine'
        self.request_method = RequestMethod()

    def deletebot(self):
        '''res 返回请求结果'''
        res = self.request_method.run_main("DELETE",self.new_url,self.request_data,self.header)
        res_json = json.loads(res)          # 转换为字典格式
        ret_msg = res_json["ret_msg"]       # 接口成功返回信息
        return ret_msg



