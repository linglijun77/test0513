# -*- coding: utf-8 -*-
# @File    : openapi.py
import time
import json
from Base.sendmail import sendMail
from Base.logger import Logger
from Base.replace_data import ReplaceData
from Base.request_method import RequestMethod
from Base.ReadExcel import ReadExcel
from Config.request_data import RequestData
from Config.request_header import RequestHeader
from Config.request_url import ReqeustUrl
from Base.WriteExcel import WriteResultData



class OpenApi(object):
    def __init__(self):
        self.url = ReqeustUrl.openapi_url
        replace_data = ReplaceData()
        self.requestdata = RequestData()
        self.request_data = self.requestdata.openapi_request_data
        self.header =replace_data.replace_openapi_header()
        self.openapi_dialogue_data_path = self.requestdata.openapi_dialogue_data_path
        self.Save_Result = []
        self.readexcel = ReadExcel(self.openapi_dialogue_data_path)
        self.request_method = RequestMethod()
        self.replace_data = ReplaceData()

    def run_openapi(self):
        Total_Data = self.readexcel.Read_Total_Data()

        for row in range(len(Total_Data)):
            time.sleep(1)
            '''获取每行index的数值'''
            row_value = Total_Data[row]
            row_index = int(row_value[0])
            '''标准问题'''
            if row_index == 0:
                '''获取标准问题'''
                value = row_value[1]
                '''替换对话数据'''
                request_data = self.replace_data.replace_openapi_request_data(value)
                try:
                    response_data = self.request_method.run_main("POST",self.url,request_data,self.header)
                    response_data = json.loads(response_data)

                    response_answer = response_data["data"][0]["value"]
                    response_module = response_data["info"]["module"]

                    '''从excel中读取answer'''
                    excel_answer = row_value[3]

                    '''进行判断'''
                    if response_module == "faq" and excel_answer == response_answer:
                        row_value.append("Pass")
                        self.Save_Result.append(row_value)
                    else:
                        row_value.append("Fail")
                        row_value.append(response_answer)           # 写入正确的答案
                        self.Save_Result.append(row_value)
                except:
                    pass
            elif row_index == 1:
                '''Function 技能'''
                value = row_value[1]
                request_data = self.replace_data.replace_openapi_request_data(value)
                try:
                    response_data = self.request_method.run_main("POST", self.url, request_data, self.header)
                    response_data = json.loads(response_data)
                    response_module = response_data["info"]["source"]
                    response_answer = response_data["data"][0]["value"]
                    '''从excel中读取answer'''
                    excel_source = row_value[2]
                    '''进行判断'''
                    if response_module == excel_source:
                        row_value.append("Pass")
                        self.Save_Result.append(row_value)
                    else:
                        row_value.append("Fail")
                        row_value.append(response_answer)
                        self.Save_Result.append(row_value)
                except:
                    pass
            elif row_index == 2:
                '''机器人形象'''
                value = row_value[1]
                request_data = self.replace_data.replace_openapi_request_data(value)
                try:
                    response_data = self.request_method.run_main("POST", self.url, request_data, self.header)
                    response_data = json.loads(response_data)
                    response_module = response_data["info"]["module"]
                    response_source = response_data["info"]["source"]
                    response_answer = response_data["data"][0]["value"]


                    '''从excel中读取answer'''
                    excel_answer = row_value[2]

                    '''进行判断'''
                    if response_module == "chat" and response_source == "robot_custom" and response_answer == excel_answer:
                        row_value.append("Pass")
                        self.Save_Result.append(row_value)
                    else:
                        row_value.append("Fail")
                        row_value.append(response_answer)
                        self.Save_Result.append(row_value)
                except:
                    pass
            elif row_index == 3:
                '''chat 闲聊'''
                value = row_value[1]
                request_data = self.replace_data.replace_openapi_request_data(value)
                try:
                    response_data = self.request_method.run_main("POST", self.url, request_data, self.header)
                    response_data = json.loads(response_data)
                    response_module = response_data["info"]["module"]
                    response_answer = response_data["data"][0]["value"]

                    '''进行判断'''
                    if response_module == "chat":
                        row_value.append("Pass")
                        self.Save_Result.append(row_value)
                    else:
                        row_value.append("Fail")
                        row_value.append(response_answer)
                        self.Save_Result.append(row_value)
                except:
                    pass
            elif row_index == 4:
                '''意图触发TDE'''
                value = row_value[1]
                request_data = self.replace_data.replace_openapi_request_data(value)
                try:
                    response_data = self.request_method.run_main("POST", self.url, request_data, self.header)
                    response_data = json.loads(response_data)
                    response_module = response_data["info"]["module"]
                    response_answer = response_data["data"][0]["value"]

                    '''从excel中读取answer'''
                    excel_answer = row_value[3]

                    '''进行判断'''
                    if response_module == "task_engine" and excel_answer == response_answer:
                        row_value.append("Pass")
                        self.Save_Result.append(row_value)
                    else:
                        row_value.append("Fail")
                        row_value.append(response_answer)
                        self.Save_Result.append(row_value)
                except:
                    pass
            elif row_index == 5:
                '''指令配置'''
                value = row_value[1]
                request_data = self.replace_data.replace_openapi_request_data(value)
                try:
                    response_data = self.request_method.run_main("POST", self.url, request_data, self.header)
                    response_data = json.loads(response_data)
                    response_module = response_data["info"]["module"]
                    response_answer1 = response_data["data"][0]["value"]

                    '''从excel中读取answer'''
                    excel_answer1 = row_value[3]
                    excel_model = row_value[2]

                    '''进行判断'''
                    if excel_answer1 == response_answer1 and response_module == excel_model:
                        row_value.append("Pass")
                        self.Save_Result.append(row_value)
                    else:
                        row_value.append("Fail")
                        row_value.append(response_answer1)
                        self.Save_Result.append(row_value)
                except:
                    pass
            elif row_index == 6:
                '''敏感词出话测试'''
                value = row_value[1]
                request_data = self.replace_data.replace_openapi_request_data(value)
                try:
                    response_data = self.request_method.run_main("POST", self.url, request_data, self.header)
                    response_data = json.loads(response_data)
                    response_answer = response_data["data"][0]["value"]
                    response_module = response_data["info"]["module"]

                    '''从excel中读取answer'''
                    excel_answer = row_value[3]
                    excel_model = row_value[2]

                    '''进行判断'''
                    if response_answer == excel_answer and response_module == excel_model:
                        row_value.append("Pass")
                        self.Save_Result.append(row_value)
                    else:
                        row_value.append("Fail")
                        row_value.append(response_answer)
                        self.Save_Result.append(row_value)
                except:
                    pass
            elif row_index == 7:
                '''知识图谱'''
                value = row_value[1]
                request_data = self.replace_data.replace_openapi_request_data(value)
                try:
                    response_data = self.request_method.run_main("POST", self.url, request_data, self.header)
                    response_data = json.loads(response_data)
                    response_answer = response_data["data"][0]["value"]
                    response_module = response_data["info"]["module"]

                    '''从excel中读取answer'''
                    excel_answer = row_value[2]
                    excel_model = row_value[3]

                    '''进行判断'''
                    if response_answer == excel_answer and response_module == excel_model:
                        row_value.append("Pass")
                        self.Save_Result.append(row_value)
                    else:
                        row_value.append("Fail")
                        row_value.append(response_answer)
                        self.Save_Result.append(row_value)
                except:
                    pass
            elif row_index == 8:
                '''意图引擎'''
                value = row_value[1]
                request_data = self.replace_data.replace_openapi_request_data(value)
                try:
                    response_data = self.request_method.run_main("POST", self.url, request_data, self.header)
                    response_data = json.loads(response_data)
                    response_intent = response_data["info"]["intent"]

                    '''从excel中读取answer'''
                    excel_intent = row_value[2]

                    '''进行判断'''
                    if response_intent == excel_intent:
                        row_value.append("Pass")
                        self.Save_Result.append(row_value)
                    else:
                        row_value.append("Fail")
                        row_value.append(response_intent)
                        self.Save_Result.append(row_value)
                except:
                    pass
            elif row_index == 9:
                '''第三方闲聊'''
                value = row_value[1]
                request_data = self.replace_data.replace_openapi_request_data(value)
                try:
                    response_data = self.request_method.run_main("POST", self.url, request_data, self.header)
                    response_data = json.loads(response_data)
                    response_module = response_data["info"]["module"]
                    response_answer = response_data["data"][0]["value"]

                    '''从excel中读取answer'''
                    excel_answer = row_value[2]
                    excel_module = row_value[3]

                    '''进行判断'''
                    if response_module == excel_module and excel_answer == response_answer:
                        row_value.append("Pass")
                        self.Save_Result.append(row_value)
                    else:
                        row_value.append("Fail")
                        row_value.append(response_answer)
                        self.Save_Result.append(row_value)
                except:
                    pass
            elif row_index == 10:
                '''同义词转换'''
                value = row_value[1]
                request_data = self.replace_data.replace_openapi_request_data(value)
                try:
                    response_data = self.request_method.run_main("POST", self.url, request_data, self.header)
                    response_data = json.loads(response_data)
                    response_module = response_data["info"]["module"]
                    response_answer = response_data["data"][0]["value"]

                    '''从excel中读取answer'''
                    excel_answer = row_value[3]
                    excel_module = row_value[2]

                    '''进行判断'''
                    if response_module == excel_module and excel_answer == response_answer:
                        row_value.append("Pass")
                        self.Save_Result.append(row_value)
                    else:
                        row_value.append("Fail")
                        row_value.append(response_answer)
                        self.Save_Result.append(row_value)
                except:
                    pass
        #将测试结果写入到excel中
        write = WriteResultData(self.Save_Result,self.requestdata.openapi_dialogue_data_result_path)
        write.WriteExcel()
        # 发送邮件
        # sendMail()




if __name__ == "__main__":
    run_openapi = OpenApi()
    run_openapi.run_openapi()



































