# -*- coding: utf-8 -*-
# @File    : request_url.py
from Config import config_url
global base_url
base_url = config_url.base_url

class ReqeustUrl(object):
    login_url = base_url + "/auth/v3/login"
    # 116环境：
    createbot_url = base_url + "/auth/v6/enterprise/bb3e3925f0ad11e7bd860242ac120003/app"
    deletebot_url = base_url + "/auth/v3/enterprise/bb3e3925f0ad11e7bd860242ac120003/app/"
    # BFOP环境
    # createbot_url = base_url + "/auth/v3/enterprise/d5603cc40d1f48ff954419b8b7a3cde8/app"
    # deletebot_url = base_url + "/auth/v3/enterprise/d5603cc40d1f48ff954419b8b7a3cde8/app/"



    upload_sq_url = base_url + "/faq/ssm/dac/upload"
    upload_lq_url = base_url + "/faq/ssm/dac/upload"
    train_sq = base_url + "/faq/ssm/dac/train"
    faq_publish = base_url + "/faq/ssm/dac/release/online"
    answer_publish = base_url + "/faq/ssm/dac/answer/release"
    set_solution_stage_status = base_url + "/solution_stage_status/set"
    upload_intent_url = base_url + "/api/v2/intents/import"
    intent_train_url = base_url + "/api/v2/intents/train?engine=intent_engine"
    intent_train_complate_url1 = base_url + "/api/v1/intent_tests/status"
    intent_train_complate_url2 = base_url + "/api/v2/intents/status"
    upload_wordbank_url = base_url + "/adm/wordbank/v2/uploadHistory/uploadFile"
    get_chatskill_url = base_url + "/api/v2/robot/chats"
    sensitive_word_url = base_url + "/api/v2/robot/chat/"
    scenario_json_upload_url = base_url + "/php/api/ApiKey/scenario_json_upload.php"
    task_engine_app_url = base_url + "/php/api/ApiKey/task_engine_app.php"
    task_engine_scenario_url = base_url + "/php/api/ApiKey/task_engine_scenario.php"
    task_engine_trigger_intent_url = base_url + "/api/v1/task/scenario/intents"
    bf_access_token_url = base_url + "/api/v1/bf/access-token"
    openapi_url = base_url + ':8080/v1/openapi'
    command_url = base_url+"/api/v1/bf/cmd"
    robot_profile = base_url+"/api/v3/robot/qa/1/answer"
    create_bot_app = base_url + "/api/v1/bf/app"
    create_bot_data = base_url + "/api/v2/robot/data"
    create_bot_ssm_data = base_url + '/api/v1/bf/ssm-data'
    function_url = base_url + "/api/v2/robot/functions"
    ssm_upload_sq_id = base_url + "/faq/ssm/dac/upload/"
    ssm_upload_lq_id = base_url + "/faq/ssm/dac/upload/"
    ssm_train_process_url = base_url + "/faq/ssm/dac/trainhistory/"
    ssm_publish_process_url = base_url + "/faq/ssm/dac/release/progress/"
    upload_kg_url = base_url + "/xeonKgDal/"
    train_kg_url = base_url + "/xeonKgDal/"
    train_kg_process_url = base_url + '/xeonKgDal/'
    verify_train_kg_finsh = base_url + '/xeonKgDal/'
    upload_third_chat_sq = base_url + "/api/v1/customchat/import/question"
    upload_third_chat_lq = base_url + "/api/v1/customchat/import/extend"


    # 中控简本
    ccs_generator_url = base_url + ":16256/ccsDal/bfopConfGenerate"

    ccs_generator_activate = base_url + ":16256/ccsDal/ccsConf/csbot/activate"






