# -*- coding: utf-8 -*-
# @File    : request_header.py
class RequestHeader(object):
    header = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b20iOnsiaWQiOiI0YjIxMTU4YTM5NTMxMWU4OGE3MTAyNDJhYzExMDAwMyIsInVzZXJfbmFtZSI6ImNzYm90YWRtaW4iLCJkaXNwbGF5X25hbWUiOiJDU0JPVDEiLCJlbWFpbCI6ImNzYm90YWRtaW5AZW1vdGlib3QuY29tIiwicGhvbmUiOiIiLCJ0eXBlIjoxLCJyb2xlcyI6eyJncm91cHMiOltdLCJhcHBzIjpbXX0sInByb2R1Y3QiOltdLCJlbnRlcnByaXNlIjoiYmIzZTM5MjVmMGFkMTFlN2JkODYwMjQyYWMxMjAwMDMiLCJzdGF0dXMiOjEsImN1c3RvbSI6bnVsbH0sImV4cCI6MTU1MzE1MTM5MiwiaXNzIjoic2ltcGxlLWF1dGgiLCJuYmYiOjE1NTMwNjQ5OTJ9.PbB2PU4spwcD_WwBwhYfIYFIbChLf4BpDSvlXacbQac",
        "Content-Type": "application/x-www-form-urlencoded",
        'Access_token': '3c46ad5c29eaa7bc2f1c5e870057135f-c20b94916eaacf9fffeba7ddfaa2b21d14fa6b74'
    }

    openapi_header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "appid": "2f02f0b352144a9c9232f13a7a45f30d",
        "userid": "12"
    }

    upload_ssm_header = {
	"app_id": "csbot",
	"user_id": "wsp",
	"locale": "zh-cn"
    }
    ssm_train_header = {
	"Content-Type": "application/json",
	"app_id": "csbot",
	"user_id": "wsp"
    }
    ssm_publish_header =  {
	"app_id": "csbot",
	"user_id": "wsp"
    }

    ccs_generator_header = {
	"Content-Type": "application/json"
}

