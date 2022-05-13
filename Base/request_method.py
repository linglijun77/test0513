# -*- coding: utf-8 -*-
# @File    : request_method.py
import json
import requests
from urllib3 import encode_multipart_formdata

class RequestMethod(object):
    def post_main(self,url,data=None,header=None):
        '''post 请求'''
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url,data=data)
        '''将请求结果设置为json格式'''
        return res.json()

    def get_main(self,url,data=None,header=None):
        '''get 请求'''
        res = None
        if header != None:
            res = requests.get(url=url,data=data,headers=header)
        else:
            res = requests.get(url=url,data=data)

        '''将请求结果设置为json格式'''
        return res.json()

    def get_delete(self,url,data=None,header=None):
        '''delete 请求'''
        res = None
        if header != None:
            res = requests.delete(url=url,data=data,headers=header)
        else:
            res = requests.delete(url=url,data=data)
        '''将请求结果设置为json格式'''
        return res.json()

    def put_main(self, url, data=None, header=None):
        '''put 请求'''
        res = None
        if header != None:
            res = requests.put(url=url, data=data, headers=header)
        else:
            res = requests.put(url=url, data=data)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        '''执行哪种请求的方法'''
        res = None
        if method == "POST":
            res = self.post_main(url,data,header)
        elif method == "GET":
            res = self.get_main(url, data, header)
        elif method == "PUT":
            res = self.put_main(url, data, header)
        else:
            res = self.get_delete(url,data,header)

        '''设置json返回数据的格式，以字典的格式显示，inden=2 表示成对显示'''
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)

    ''' 上传文件 '''
    def upload_file(self, url, header=None, data=None, fileKey=None, filePath=None):
        if fileKey is not None:
            data[fileKey] = ('a.xlsx', open(filePath, 'rb').read())
        encode_data = encode_multipart_formdata(data)
        header['Content-Type'] = encode_data[1]

        res = requests.post(url=url, headers=header, data=encode_data[0])

        return res.json()
