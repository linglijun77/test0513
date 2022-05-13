# -*- coding: utf-8 -*-
# @File    : createbot.py
import time
import json

from Config.request_data import RequestData
from Config.request_url import ReqeustUrl
from Config.request_header import RequestHeader
from Base.replace_data import ReplaceData
from Base.request_method import RequestMethod

class UploadLQ(object):
    def __init__(self):
        self.url = ReqeustUrl.upload_lq_url
        self.request_data = RequestData.upload_lq_data
        self.request_method = RequestMethod()
        # 替换SSM 中的header
        self.header = RequestHeader.upload_ssm_header
        self.header["app_id"] = RequestData.appid
        self.header["user_id"] = RequestData.userid


    def uploadLQ(self):
        # res 返回请求结果
        fileKey = 'file'
        filePath = './files/upload_lq.xlsx'
        res = self.request_method.upload_file(self.url, self.header, self.request_data, fileKey, filePath)
        # res["data"]将上传的ID写入到配置文件 upload_ssm_lq_id 变量中
        RequestData.upload_ssm_lq_id = res["data"]

        # 拼接查询语料上传进度的URL
        upload_ssm_lq_process_url =  ReqeustUrl.ssm_upload_lq_id + str(RequestData.upload_ssm_lq_id) + '?type=LQ'

        while True:
            # res = requests.get(upload_ssm_sq_process_url)
            res = self.request_method.run_main("GET", url=upload_ssm_lq_process_url, header=self.header)
            res = json.loads(res)  # 转换为字典格式，在进行提取process

            if int(res["data"]["progress"]) == int(100):
                time.sleep(5)
                return res["data"]["progress"]
            else:
                continue
