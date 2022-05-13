# -*- coding: utf-8 -*-
# @File    : knowledge.py
import time
import json

from Base.replace_data import ReplaceData
from Base.request_method import RequestMethod
from Config.request_data import RequestData
from Config.request_url import ReqeustUrl
from Config.request_header import RequestHeader


class KnowledgeGraph(object):
    def __init__(self):
        self.url = ReqeustUrl.upload_kg_url + str(RequestData.appid) + "/import/all"
        self.request_data = RequestData.upload_kg_data
        '''替换header请求数据中的token'''
        replace_data = ReplaceData()
        # 替换token后，获取header
        self.header = replace_data.replace_token()
        self.request_method = RequestMethod()

    def uploadKG(self):
        # res 返回请求结果
        fileKey = 'file'
        filePath = './files/knowledge.xlsx'

        res = self.request_method.upload_file(url=self.url, header=self.header,data=self.request_data,fileKey=fileKey,filePath=filePath)
        # 返回上传的状态
        return  res["status"]

    def trainKG(self):
        self.train_kg_url = ReqeustUrl.train_kg_url + str(RequestData.appid) + "/ftTrainTrigger?env=sandbox"

        res = self.request_method.run_main("GET",url=self.train_kg_url,header=self.header)
        # 将回答转换为字典格式
        res = json.loads(res)

        # 查询KG训练进度
        self.train_kg_process_url = ReqeustUrl.train_kg_process_url + str(RequestData.appid) + "/ftTrainResult/" + res["taskId"]


        while True:
            res = self.request_method.run_main("GET",url=self.train_kg_process_url,header=self.header)
            # 将格式转换为自带你格式
            res = json.loads(res)

            if res["status"] == "done":
                break
                # return res["status"]
            else:
                continue

        # 验证训练是否完成
        self.verify_train_finish_url = ReqeustUrl.verify_train_kg_finsh + str(RequestData.appid) + '/synchronizeSandbox'

        self.verify_train_finish_data = RequestData.verify_train_kg_data

        res = self.request_method.run_main("POST",url=self.verify_train_finish_url,data=self.verify_train_finish_data,header=self.header)

        res = json.loads(res)

        return res["status"]















