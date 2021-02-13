from _pytest.mark import param
import yaml
import logging
import json
from jsonpath import jsonpath
import requests
from requests import request


class BaseApi:
    #格式化字符串
    @classmethod
    def format(cls,r):
        #存储r，后续需要调用r的部分就可以省略r的引用
        cls.r=r
        # print(json.dumps(r.json(),indent=2))
        # 格式化，且把中文正常展示(展示unicode原始形式，而不是unicode的编码)
        print(json.dumps(json.loads(r.text),indent=2,ensure_ascii=False))

    #取reponse中path匹配
    def jsonpath(self,path,r=None):
        #省略传r的步骤(因为format方法引入了r)
        if r is None:
            r=self.r.json()
        return jsonpath(r,path)

    #封装yaml文件的加载
    #——> lsit是指定返回类型是list
    @classmethod
    def yaml_load(self,path)->list:
        with open(path) as f:
            return yaml.safe_load(f)

    #读取yaml文件内容
    def api_load(self,path):
        return self.yaml_load(path)

    #把读取到的内容拆解成参数
    def api_send(self,req:dict):
        req['params']['access_token']=self.get_token()
        #此种方法用于请求方式未知的的情况
        r=requests.request(
            req["method"],
            url=req['url'],
            params=req['params'],
            json=req['json']
        )
        self.format(r)
        return r.json()

