# -*- coding: utf-8 -*-
import json
import time

from Config.request_data import RequestData
from Config.request_url import ReqeustUrl
from Base.replace_data import ReplaceData
from Base.request_method import RequestMethod
from urllib3 import encode_multipart_formdata
import requests

class IntentOperation(object):
    def __init__(self):
        self.uploadurl = ReqeustUrl.upload_intent_url
        self.trainurl = ReqeustUrl.intent_train_url
        self.intent_train_complate_url1 = ReqeustUrl.intent_train_complate_url1
        self.intent_train_complate_url2 = ReqeustUrl.intent_train_complate_url2
        self.upload_intent_path = RequestData.upload_intent_path
        self.request_data = RequestData.upload_intent_data

        replace_data = ReplaceData()
        self.header = replace_data.replace_token()              # 替换token后，获取header
        self.request_method = RequestMethod()

    def uploadIntent(self):
        fileKey = 'file'
        filePath = './Files/intent.xlsx'
        res = self.request_method.upload_file(self.uploadurl, self.header, self.request_data, fileKey, filePath)

        return res['status']


    def trainIntent(self):
        res = requests.post(url=self.trainurl, headers=self.header).json()

        while True:

            time.sleep(1)
            # 第一个测试请求
            requests.get(url=self.intent_train_complate_url1, headers=self.header)
            # 第二个判断训练的进度
            res = requests.get(url=self.intent_train_complate_url2,headers=self.header).json()

            # res["result"]["progress"] 每秒请求一次，判断上传的进度是否到达100%
            if res["result"]["progress"] == 100:
                return res["result"]["progress"]
            else:
                continue

