import json
import logging
import requests
from datetime import datetime, date
from decimal import Decimal

# 自定义 JSON 编码器
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(obj, date):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)

class WebRequests(object):

    def __init__(self):
        pass

    @staticmethod
    def get(url, params=None, headers=None, files=None, cookies=None):
        """封装get方法，return响应码和响应内容"""
        try:
            logging.info("get url：%s" % url)
            logging.info("请求header：%s" % headers)
            logging.info("请求body：%s" % params)
            response = requests.get(url, params=params, headers=headers, files=files, cookies=cookies)
            status_code = response.status_code  # 获取返回的状态码
            logging.info("获取返回的状态码:%d" % status_code)
            # 如果返回不是json格式，则不转换，直接返回内容
            if '<!DOCTYPE html>' in str(response.content.decode('utf-8')) or '<!doctype html>' in str(response.content.decode('utf-8')):
                logging.info("响应内容：%s" % str(response.content))
                return status_code, str(response.content)
            else:
                response_json = response.json()  # 响应内容，json类型转化成python数据类型
                logging.info("响应内容：%s" % response_json)
                return status_code, response_json  # 返回响应码，响应内容
        except BaseException as e:
            logging.error("请求失败！", exc_info=1)

    @staticmethod
    def post(url, data=None, headers=None, cookies=None, data_to_json=True):
        """封装post方法，并用json格式传值，return响应码和响应内容"""
        try:
            logging.info("post url：%s" % url)
            logging.info("请求header：%s" % headers)
            logging.info("请求body：%s" % data)
            if data_to_json:
                data = json.dumps(data, cls=CustomEncoder).encode('utf-8')  # python数据类型转化为json数据类型
            response = requests.post(url, data=data, headers=headers, cookies=cookies)
            status_code = response.status_code  # 获取返回的状态码
            logging.info("获取返回的状态码:%d" % status_code)
            response_json = response.json()  # 响应内容，json类型转化成python数据类型
            logging.info("响应内容：%s" % response_json)
            return status_code, response_json  # 返回响应码，响应内容
        except BaseException as e:
            logging.error("请求失败！", exc_info=1)

    @staticmethod
    def put(url, data=None, headers=None):
        """封装put方法，如果含有“{”则用json格式传值，否则直接传递，return响应码和响应内容"""
        try:
            logging.info("put url：%s" % url)
            logging.info("请求header：%s" % headers)
            logging.info("请求body：%s" % data)
            if '{' in data and '}' in data:
                data = json.dumps(data).encode('utf-8')  # python数据类型转化为json数据类型
            response = requests.put(url, data=data, headers=headers)
            status_code = response.status_code  # 获取返回的状态码
            logging.info("获取返回的状态码:%d" % status_code)
            response_json = response.json()  # 响应内容，json类型转化成python数据类型
            logging.info("响应内容：%s" % response_json)
            return status_code, response_json  # 返回响应码，响应内容
        except BaseException as e:
            logging.error("请求失败！", exc_info=1)

    @staticmethod
    def delete(url, data=None, headers=None):
        """封装delete方法，并用json格式传值，return响应码和响应内容"""
        try:
            logging.info("delete url：%s" % url)
            logging.info("请求header：%s" % headers)
            logging.info("请求body：%s" % data)
            data = json.dumps(data).encode('utf-8')  # python数据类型转化为json数据类型
            response = requests.delete(url, data=data, headers=headers)
            status_code = response.status_code  # 获取返回的状态码
            logging.info("获取返回的状态码:%d" % status_code)
            response_json = response.json()  # 响应内容，json类型转化成python数据类型
            logging.info("响应内容：%s" % response_json)
            return status_code, response_json  # 返回响应码，响应内容
        except BaseException as e:
            logging.error("请求失败！", exc_info=1)

