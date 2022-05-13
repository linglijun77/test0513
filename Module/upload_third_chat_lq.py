# -*- coding: utf-8 -*-
# @File    : upload_third_chat_lq.py
import time
import requests
import json

from Config.request_data import RequestData
from Config.request_url import ReqeustUrl
from Config.request_header import RequestHeader
from Base.request_method import RequestMethod
from Base.replace_data import ReplaceData


class UploadThirdChatLQ(object):
    def __init__(self):
        self.url = ReqeustUrl.upload_third_chat_lq
        self.request_data = RequestData.upload_third_chat_lq
        self.request_method = RequestMethod()

        # 替换header
        replace_data = ReplaceData()
        self.header = replace_data.replace_token()  # 替换token后，获取header
        self.request_method = RequestMethod()

    def UploadThirdChatLq(self):
        # res 返回请求结果

        fileKey = 'file'
        filePath = './Files/third_chat_lq.xlsx'
        res = self.request_method.upload_file(self.url, self.header, self.request_data, fileKey, filePath)

        # 返回结果
        return res["result"]
