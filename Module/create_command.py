# -*- coding: utf-8 -*-
# @File    : createbot.py
import json

import unittest

from Config.request_data import RequestData
from Config.request_url import ReqeustUrl
from Base.replace_data import ReplaceData
from Base.request_method import RequestMethod


class CreateCommnad(object):
    def __init__(self):
        self.url = ReqeustUrl.command_url
        self.create_cmd_data = RequestData.create_cmd_data
        self.active_cmd_data = RequestData.active_cmd_data
        '''替换header请求数据中的token'''
        replace_data = ReplaceData()
        self.header = replace_data.replace_token()  # 替换token后，获取header
        self.request_method = RequestMethod()

    def createCommand(self):
        # res 返回请求结果
        res = self.request_method.run_main("POST", self.url, self.create_cmd_data, self.header)

        # 转换为字典格式
        res_json = json.loads(res, encoding='utf-8')

        id = res_json["result"]["id"]
        res = self.request_method.run_main("PUT", self.url + "/" + str(id), self.active_cmd_data, self.header)

    # 接口成功返回信息
        ret_msg = res_json['status']
        # print type(ret_msg)
        # print ret_msg

        # RequestData.appid = res_json["result"]["id"]     # 获取创建机器人的appid

        return ret_msg
