# -*- coding: utf-8 -*-
# @File    : ssm_publish.py
import time
import json

from Config.request_data import RequestData
from Config.request_url import ReqeustUrl
from Config.request_header import RequestHeader
from Base.replace_data import ReplaceData
from Base.request_method import RequestMethod

class SSMPublish(object):
    def __init__(self):
        self.faq_publish_url = ReqeustUrl.faq_publish
        self.answer_publish_url = ReqeustUrl.answer_publish
        self.request_method = RequestMethod()
        # 替换SSM 中的header
        self.header = RequestHeader.ssm_publish_header
        self.header["app_id"] = RequestData.appid
        self.header["user_id"] = RequestData.userid

    def SSMPublish(self):
        # 调用faq发布接口
        res = self.request_method.run_main("GET",url=self.faq_publish_url,header=self.header)
        # 获取训练进度的ID
        res = json.loads(res)
        RequestData.publish_id = res["data"]

        # 调用回答发布接口
        while True:
            res1 = self.request_method.run_main("GET",url=self.answer_publish_url,header=self.header)

            res1 = json.loads(res1)
            if res1["message"] == "成功":
                break
            else:
                continue

        # 拼接查询训练进度的URL
        train_process_url = str(ReqeustUrl.ssm_publish_process_url) + str(RequestData.publish_id)

        while True:
            res = self.request_method.run_main("GET", url=train_process_url, header=self.header)

            res = json.loads(res)  # 转换为字典格式，在进行提取process
            if int(res["data"]) == int(100):
                time.sleep(5)
                return res["data"]
            else:
                continue
