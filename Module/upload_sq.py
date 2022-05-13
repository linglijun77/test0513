# -*- coding: utf-8 -*-
# @File    : createbot.py
import time
import requests
import json

from Config.request_data import RequestData
from Config.request_url import ReqeustUrl
from Config.request_header import RequestHeader
from Base.replace_data import ReplaceData
from Base.request_method import RequestMethod


class UploadSQ(object):
    def __init__(self):
        self.url = ReqeustUrl.upload_sq_url
        self.request_data = RequestData.upload_sq_data
        self.request_method = RequestMethod()
        self.header = RequestHeader.upload_ssm_header
        # 替换SSM 中的header
        self.header["app_id"] = RequestData.appid
        self.header["user_id"] = RequestData.userid

    def uploadSQ(self):
        # res 返回请求结果

        fileKey = 'file'
        filePath = './Files/upload_sq.xlsx'
        res = self.request_method.upload_file(self.url, self.header, self.request_data, fileKey, filePath)

        # 提取上传进度
        RequestData.upload_ssm_sq_id = res["data"]

        # 拼接标准问上传进度的URL
        upload_ssm_sq_process_url = ReqeustUrl.ssm_upload_sq_id + str(RequestData.upload_ssm_sq_id) + "?type=SQ_ANS"

        while True:
            # time.sleep(0.5)
            # res = requests.get(upload_ssm_sq_process_url)
            res = self.request_method.run_main("GET",url=upload_ssm_sq_process_url,header=self.header)
            res = json.loads(res)       # 转换为字典格式，在进行提取process

            if int(res["data"]["progress"]) == int(100):
                time.sleep(5)
                return res["data"]["progress"]
            else:
                continue
