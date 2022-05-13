# -*- coding: utf-8 -*-
# @File    : replace_data.py
import time
import json

from Config.request_data import RequestData
from Config.request_header import RequestHeader


class ReplaceData(object):
    def __init__(self):
        self.token = RequestData.token
        self.appId = RequestData.appid
        self.bf_access_token = RequestData.bf_access_token
        self.userid = RequestData.userid
        self.openapi_request_data = RequestData.openapi_request_data

    def replace_token(self):
        '''
        替换请求中的token值
        :param old_header:请求header
        :param old_token: 被替换的key
        :param new_token: 替换的value
        :return:
        '''
        header = RequestHeader.header
        header["Authorization"] = self.token
        header["Access_token"] = RequestData.access_token
        header["X-Appid"]=self.appId
        header["user_id"] = self.userid
        RequestHeader.header = header       #将替换后的header 写入到requestheader 配置文件中

        return header

    def join_token(self,token):
        '''
        # 获取系统返回的token，并将token + Bearer 拼接完整token字符串，并赋给变量token
        :return:
        '''
        new_token = "Bearer" + " " + token
        return new_token

    def get_wordbank_header(self):
        header = RequestHeader.header
        header["X-Appid"] = RequestData.appid
        header["Content-Type"] = "multipart/form-data"
        return header

    def replace_openapi_header(self):
        '''替换openapi中的appid以及userid'''
        openapi_header = RequestHeader.openapi_header
        openapi_header["appid"] =  self.appId
        openapi_header["userid"] = self.userid

        return openapi_header


    def replace_openapi_request_data(self,request_text):
        '''替换对话接口中的请求数据'''
        self.openapi_request_data["text"] = request_text

        #返回json格式的请求数据
        return json.dumps(self.openapi_request_data)

    def replace_create_bot_app(self):
        '''替换create_bot_app请求中的appid'''
        create_bot_app_data = RequestData.create_bot_app
        create_bot_app_data["appid"] = self.appId
        create_bot_app_data["userid"] = self.userid
        RequestData.create_bot_app = create_bot_app_data

        return create_bot_app_data

    def replace_create_bot_ssm_data(self):
        '''替换create_bot_ssm_data请求中的数据'''
        create_bot_ssm_data = RequestData.create_bot_ssm_data
        create_bot_ssm_data["appid"] = self.appId
        RequestData.create_bot_ssm_data = create_bot_ssm_data

        return create_bot_ssm_data

