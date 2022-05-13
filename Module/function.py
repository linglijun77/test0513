# -*- coding: utf-8 -*-
# @File    : function.py
import json
import requests
from Base.logger import Logger
from Config.request_data import RequestData
from Config.request_header import RequestHeader
from Config.request_url import ReqeustUrl
from Base.replace_data import ReplaceData
from Base.request_method import RequestMethod

class OpenFunctionSwitch(object):
    def __init__(self):
        self.url = ReqeustUrl.function_url
        self.request_data = RequestData.function_request_data
        self.header = RequestHeader.header
        self.request_method = RequestMethod()

    def function_switch(self):
        res = self.request_method.run_main("POST",self.url,self.request_data,self.header)
        res_json = json.loads(res)  # 转换为字典格式
        res_msg = res_json["message"]
        return res_msg