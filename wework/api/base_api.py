import yaml
import logging
import json
from jsonpath import jsonpath
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

    #todo:封装类似HttpRunner这样的数据驱动框架
    def steps(self,path):
        with open(path) as f:
            steps: list[dict] = yaml.safe_load(f)
            # request: Request = None
