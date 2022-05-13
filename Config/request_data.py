# -*- coding: utf-8 -*-
# @File    : request_data.py
import os
class RequestData(object):
    # BFOP 线上换机功能
    # login_request_data = {
    #     "account": "testadmin",
    #     "passwd": "e64b78fc3bc91bcbc7dc232ba8ec59e0",
    #     "captcha": ""
    # }

    # 116环境账号密码
    login_request_data = {
    "account": "csbotadmin",
    "passwd": "ac04367d3155bb651df2e4220bdb8303",
    "captcha": ""
    }


    token = ''
    access_token = ''
    enterprise = ''
    create_bot_data = {
        "name": "20200112",
        "description": "",
        "props":"[{\"id\":\"1\"}]"
    }

    #BFOP 上面的appid
    appid = ''
    # 116环境的测试
    # appid = '1803a0c6ae484aef88231b6ab5f1a630'
    # 上传标准问id
    upload_ssm_sq_id = ""
    # 语料上传ID
    upload_ssm_lq_id = ""
    # 训练ID
    train_id = ""
    # 发布ID
    publish_id = ""


    bf_access_token = ''
    delete_bot_data = {}
    openapi_request_data = {
	"text": "LY测试机器人的验证"
    }
    userid = 'bb3e3925f0ad11e7bd860242ac120003'
    openapi_dialogue_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)) + '/Files/automatic_file.xls'
    openapi_dialogue_data_result_path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)) + '/Files/general_result.xls'



    upload_sq_data = {
        'mode': 'incre',
        'type': 'SQ_ANS',
        'comment':'upload'
    }

    upload_lq_data = {
        'mode': 'incre',
        'type': 'LQ',
        'comment':'upload'
    }
    upload_third_chat_sq = {

    }

    upload_third_chat_lq = {

    }


    upload_intent_data = {

    }

    train_sq_data = {

    }
    upload_kg_data = {

    }

    verify_train_kg_data = {

    }

    train_finish_solution_stage = {
        'app_id': '',
        'module': 'squestionMatching',
        'stage': 4,
        'status': 'train-finished'
    }

    upload_intent_path = "../Files/intent.xlsx"
    skill_type = ""
    sensitive_word_data = {
        "content": "这是敏感词"
    }

    create_cmd_data = "name=test%40%E6%B5%8B%E8%AF%95%E7%94%A8&rule=%5B%7B%22type%22%3A%22keyword%22%2C%22value%22%3A%5B%22ping%22%5D%7D%5D&target=0&answer=pong&response_type=0&status=false&labels=%5B%5D&end_time=&cid=-1"

    active_cmd_data = "name=test%40%E6%B5%8B%E8%AF%95%E7%94%A8&rule=%5B%7B%22type%22%3A%22keyword%22%2C%22value%22%3A%5B%22ping%22%5D%7D%5D&target=0&answer=pong&response_type=0&status=true&labels=%5B%5D&begin_time=&end_time="

    robot_file_data = 'content=%E6%88%91%E6%98%AF%E6%B5%8B%E8%AF%95%E6%9C%BA%E5%99%A8%E4%BA%BA'

    create_bot_ssm_data = {
	"appid": "076f5f6d7847450bbdd65b9786179fa4"
    }

    create_bot_app = {
	"appid": "83c1d8d548574724935f4a29cf47893a",
	"userid": "4b21158a395311e88a710242ac110003",
	"name": "test-create-bot-1"
    }
    function_request_data = "active=%7B%22ComputationModule%22%3Atrue%2C%22DatetimeModule%22%3Atrue%2C%22JokeModule%22%3Atrue%2C%22QueryExchangeModule%22%3Atrue%2C%22QueryStockModule%22%3Atrue%2C%22StoryModule%22%3Atrue%2C%22WeatherModule%22%3Atrue%7D"

    ccs_generator_data = {
	"ccsId": "b02591965f874393978f43aa1da835df",
	"appId": "b02591965f874393978f43aa1da835df"
}
    ccs_generator_activate_data = {
	"id": 122
}