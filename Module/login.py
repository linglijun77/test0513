# -*- coding: utf-8 -*-
# @File    : login.py
import json

from Base.request_method import RequestMethod
from Base.replace_data import ReplaceData
from Config.request_data import RequestData
from Config.request_header import RequestHeader
from Config.request_url import ReqeustUrl



class AccoutLogin(object):
    def __init__(self):
        self.url = ReqeustUrl.login_url
        self.request_data = RequestData.login_request_data
        self.requestmethod = RequestMethod()
        self.replace_token = ReplaceData()

    def login(self):
        '''res 返回请求结果'''
        res = None
        res = self.requestmethod.run_main("POST",self.url,self.request_data)

        res_json = json.loads(res)          # 转换为字典格式
        response_token = res_json["result"]["token"]
        '''join_token 函数主要是拼接完整的token值'''
        RequestData.token = self.replace_token.join_token(response_token)
        RequestData.enterprise = res_json["result"]["info"]["enterprise"]
        RequestData.userid = res_json["result"]["info"]["id"]
        ret_msg = res_json["ret_msg"]       # 接口成功返回信息


        return ret_msg


    def bf_access_token(self):
        bf_access_token = None
        header = RequestHeader.header
        header['Authorization']=RequestData.token
        res = self.requestmethod.run_main("GET",ReqeustUrl.bf_access_token_url,self.request_data, header=header)
        res_json = json.loads(res)
        if res_json['status'] == 0:
            bf_access_token = res_json["result"]
            RequestData.bf_access_token=bf_access_token
            RequestData.access_token=bf_access_token

        return bf_access_token


