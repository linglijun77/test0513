# -*- coding: utf-8 -*-
# @File    : createbot.py
import json

from Config.request_data import RequestData
from Config.request_header import RequestHeader
from Config.request_url import ReqeustUrl
from Base.replace_data import ReplaceData
from Base.request_method import RequestMethod


class AddSensitiveWord(object):
    def __init__(self):
        self.url = ReqeustUrl.sensitive_word_url
        self.request_data = RequestData.sensitive_word_data
        '''替换header请求数据中的token'''
        replace_data = ReplaceData()
        self.header = replace_data.replace_token()              # 替换token后，获取header
        self.header["Content-Type"] = "application/x-www-form-urlencoded"
        self.header["X-Appid"] = RequestData.appid
        self.request_method = RequestMethod()

    def getChatSkills(self):
        '''res 返回请求结果'''
        res = self.request_method.run_main("GET",ReqeustUrl.get_chatskill_url,data=None,header=self.header)
        res_json = json.loads(res)              # 转换为字典格式
        ret_msg = res_json                      # 接口返回信息

        return ret_msg

    def addSensitiveAnswer(self):
        '''res 返回请求结果'''
        self.url = self.url + str(RequestData.skill_type) + "/content"
        res = self.request_method.run_main("POST", self.url, self.request_data, self.header)
        res_json = json.loads(res)  # 转换为字典格式
        ret_msg = res_json["status"]  # 接口成功返回信息

        return ret_msg





