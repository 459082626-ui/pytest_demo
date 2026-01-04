import json
import requests

from config.config import CONFIG
from exceptions.exceptions import ApiRequestError


class SmaApi:
    def __init__(self):
        self.timeout = CONFIG.TIME_OUT
        self.session = requests.Session()

    # 提取公共请求方法
    def _send_post_request(self, url, body):
        """发送POST请求的公共方法"""
        try:
            headers = {"Content-Type": "application/json; charset=utf-8"}
            response = self.session.post(url, json=body, headers=headers, timeout=self.timeout)
            response.raise_for_status()  # 自动抛出HTTP错误
            return json.loads(response.text)
        except Exception as e:
            raise ApiRequestError from e

    def submit(self, url, body):
        """原submit方法，调用公共方法"""
        response_test = self._send_post_request(url, body)
        return {
            "result": int(response_test["result"]),
            "desc": response_test["desc"]
        }

    def dfrc_submit(self, url, body):
        response_body = self._send_post_request(url, body)
        if "seqid" in response_body:
            return {
                "resultCode": int(response_body["resultCode"]),
                "resultMsg": response_body["resultMsg"],
                "msgid": response_body["msgid"],
                "seqid": response_body["seqid"]
            }
        else:
            return {
                "resultCode": int(response_body["resultCode"]),
                "resultMsg": response_body["resultMsg"],
                "msgid": response_body["msgId"]
            }

    def __del__(self):
        if hasattr(self, "session"):
            self.session.close()
