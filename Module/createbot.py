# -*- coding: utf-8 -*-
# @File    : createbot.py
import json
import requests
from Base.logger import Logger
from Config.request_data import RequestData
from Config.request_header import RequestHeader
from Config.request_url import ReqeustUrl
from Base.replace_data import ReplaceData
from Base.request_method import RequestMethod
from Config.request_data import RequestData
from Config.request_header import RequestHeader

class CreateRobot(object):
    def __init__(self):
        self.url = ReqeustUrl.createbot_url
        self.request_data = RequestData.create_bot_data
        '''替换header请求数据中的token'''
        replace_data = ReplaceData()
        self.header = replace_data.replace_token()              # 替换token后，获取header
        self.request_method = RequestMethod()


    def createbot(self):
        '''res 返回请求结果'''
        res = self.request_method.run_main("POST",self.url,self.request_data,self.header)
        res_json = json.loads(res)              # 转换为字典格式
        if res_json['result'] is not None:
            ret_msg = res_json["result"]["name"]    # 接口成功返回信息
            RequestData.appid = res_json["result"]["id"]     # 获取创建机器人的appid
        else:
            ret_msg = ''
        return ret_msg

    def assess_app(self):
        assess_app_url = ReqeustUrl.create_bot_app
        assess_app_request_data = ReplaceData().replace_create_bot_app()
        res = requests.post(url=assess_app_url,data=assess_app_request_data,headers=self.header)




    def assess_ssm_data(self):
        assess_ssm_data_url = ReqeustUrl.create_bot_ssm_data
        assess_ssm_data_request_data = ReplaceData().replace_create_bot_ssm_data()
        res = requests.post(url=assess_ssm_data_url,data=assess_ssm_data_request_data,headers=self.header)



    def assess_data(self):
        assess_data_url = ReqeustUrl.create_bot_data
        assess_data_request_data = ReplaceData().replace_create_bot_ssm_data()
        res = requests.post(url=assess_data_url, data=assess_data_request_data, headers=self.header)


    def ccs_generator(self):
        ccs_generator_url = ReqeustUrl.ccs_generator_url
        ccs_generator_data = RequestData.ccs_generator_data
        ccs_generator_data["appId"] = RequestData.appid
        ccs_generator_data["ccsId"] = RequestData.appid
        ccs_generator_header = RequestHeader.ccs_generator_header


        print ("ccs_generator_url",ccs_generator_url)
        print ("headers",ccs_generator_header)
        print ("ccs_generator_data",ccs_generator_data)
        data = json.dumps(ccs_generator_data)
        resp = requests.post(url=ccs_generator_url,headers=ccs_generator_header,data=data)

        print ("resp,",resp.text)

        resp = resp.text
        resp = json.loads(resp)
        ccs_id = resp["data"]

        ccs_generator_activate_url = ReqeustUrl.ccs_generator_activate
        ccs_generator_activate_data = RequestData.ccs_generator_activate_data
        ccs_generator_activate_header = RequestHeader.ccs_generator_header

        ccs_generator_activate_data["id"] = ccs_id

        data = json.dumps(ccs_generator_activate_data)
        resp = requests.post(url=ccs_generator_activate_url,headers=ccs_generator_activate_header,data=data)


