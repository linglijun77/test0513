# -*- coding: utf-8 -*-
# @File    : createbot.py
# import json
import requests
from urllib3 import encode_multipart_formdata
from Config.request_data import RequestData
from Config.request_url import ReqeustUrl
from Base.replace_data import ReplaceData
from Base.request_method import RequestMethod
from Config.request_data import RequestData


class UploadWordbank(object):
    def __init__(self):
        self.url = ReqeustUrl.upload_wordbank_url
        '''替换header请求数据中的token'''
        replace_data = ReplaceData()
        self.header = replace_data.get_wordbank_header()              # 获取上传词库头部
        self.request_method = RequestMethod()

    def uploadWordbank(self):
        filepath = "./Files/wordbank.xlsx"
        data = {
            "file": "(binary)",
            "appid":RequestData.appid,
            "uploadType":0
        }
        data["file"] = ("wordbank.xlsx", open(filepath, 'rb').read())
        encode_data = encode_multipart_formdata(data)
        header = self.header
        header["Content-Type"] = encode_data[1]
        # res 返回请求结果
        res = requests.post(url=self.url, headers=header, data=encode_data[0])

