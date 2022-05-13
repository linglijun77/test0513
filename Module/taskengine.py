# -*- coding: utf-8 -*-
# @File    : login.py
import json
from Base.request_method import RequestMethod
from Base.replace_data import ReplaceData
from Config.request_data import RequestData
from Config.request_url import ReqeustUrl
from urllib3 import encode_multipart_formdata
import time

class Taskengine(object):
    def __init__(self):
        self.scenario_json_upload_url = ReqeustUrl.scenario_json_upload_url
        self.task_engine_app_url = ReqeustUrl.task_engine_app_url
        self.task_engine_scenario_url = ReqeustUrl.task_engine_scenario_url
        self.task_engine_trigger_intent_url = ReqeustUrl.task_engine_trigger_intent_url
        self.requestmethod = RequestMethod()
        replace_data = ReplaceData()
        self.header = replace_data.replace_token()
    def importScenario(self):
        data = {
            "scenario_json":"(binary)",
            "appid":RequestData.appid,
            "useNewId":"true"
        }
        data['scenario_json'] = ("scenario1.json", open('./files/scenario.json', 'rb').read())
        encode_data = encode_multipart_formdata(data)
        data = encode_data[0]

        header = self.header
        header['Content-Type'] = encode_data[1]
        header['Access_token'] = RequestData.bf_access_token
        r = self.requestmethod.run_main("POST", self.scenario_json_upload_url, data, self.header)

        res_json = json.loads(r)
        return res_json


    def getAllScenarios(self):
        data = {
            "appid": RequestData.appid
        }

        header = self.header
        header['Access_token'] = RequestData.bf_access_token
        r = self.requestmethod.run_main("GET", self.task_engine_app_url, data, self.header)
        res_json = json.loads(r)

        list = []
        for item in res_json['msg']:
            list.append(item['scenarioID'])
        return list

    def openScenarios(self):
        res = True
        list = self.getAllScenarios()
        for item in list:
            publish = self.publishScenario(item)
            if publish['msg'] != 'Update success':
                res = False
            time.sleep(5)
            enable = self.enableScenario(item)
            if enable['msg'] != 'Enable success':
                res = False
        return res

    def getScenarioTriggerIntent(self, scenarioid):
        data = {
            "scenarioid": scenarioid
        }
        encode_data = encode_multipart_formdata(data)
        data = encode_data[0]

        header = self.header
        header['Content-Type'] = encode_data[1]
        header['Access_token'] = RequestData.bf_access_token
        r = self.requestmethod.run_main("GET", self.task_engine_scenario_url, data, self.header)
        res_json = json.loads(r)
        return res_json

    def enableScenario(self, scenarioid):
        data = {
            "appid": RequestData.appid,
            "scenarioid": scenarioid,
            "enable": "true",
            'method': 'POST'
        }
        encode_data = encode_multipart_formdata(data)
        data = encode_data[0]

        header = self.header
        header['Content-Type'] = encode_data[1]
        header['Access_token'] = RequestData.bf_access_token
        r = self.requestmethod.run_main("POST", self.task_engine_app_url, data, self.header)
        res_json = json.loads(r)

        return res_json

    def publishScenario(self, scenarioid):
        data = {
            "appid": RequestData.appid,
            "scenarioid": scenarioid,
            "publish": 1,
            'method': 'PUT'
        }

        header = self.header
        header['Access_token'] = RequestData.bf_access_token
        header['Content-Type'] = 'application/x-www-form-urlencoded'
        r = self.requestmethod.run_main("PUT", self.task_engine_scenario_url, data, self.header)
        res_json = json.loads(r)

        return res_json

