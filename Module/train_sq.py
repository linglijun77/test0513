# -*- coding: utf-8 -*-
# @File    : createbot.py
import time
import json

from Config.request_data import RequestData
from Config.request_url import ReqeustUrl
from Config.request_header import RequestHeader
from Base.replace_data import ReplaceData
from Base.request_method import RequestMethod

class TrainSq(object):
    def __init__(self):
        self.url = ReqeustUrl.train_sq
        self.request_data = RequestData.train_sq_data
        self.request_method = RequestMethod()
        # 替换SSM 中的header
        self.header = RequestHeader.ssm_train_header
        self.header["app_id"] = RequestData.appid
        self.header["user_id"] = RequestData.userid

    def trainSQ(self):
        # 调用训练按钮
        res = self.request_method.run_main("GET",url=self.url,header=self.header)
        # 获取训练进度的ID
        res = json.loads(res)
        RequestData.train_id = res["data"]

        # 拼接查询训练进度的URL
        train_process_url = str(ReqeustUrl.ssm_train_process_url) + str(RequestData.train_id)

        while True:
            res = self.request_method.run_main("GET", url=train_process_url, header=self.header)

            res = json.loads(res)  # 转换为字典格式，在进行提取process
            if int(res["data"]["progress"]) == int(100):
                time.sleep(10)
                return res["data"]["progress"]
            else:
                continue
