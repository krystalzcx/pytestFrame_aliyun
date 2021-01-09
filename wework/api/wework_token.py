import requests
import json
from api.base_api import BaseApi

class WeWork(BaseApi):
    token_url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    secret='g6HTdjCLPYqGL54RtfbIn1oGZcKw9SOehw9CaH1XelM'
    corpid='ww14d8a344f7e5068b'
    token=dict()
    #token时效校验
    token_time=dict()

    #每个模块的secret不相同，所以要分别存储
    @classmethod
    def get_token(cls,secret=secret):    
        #todo:
        if secret is None:
            #todo:token制度发生变化，在这个地方决定是否重新获取
            #  解决办法：存时间戳
            return cls.token[secret]
        #避免重复请求，提高速度
        if secret not in cls.token.keys():
            r=cls.get_access_token(secret)
            cls.token[secret]=r["access_token"]
            # token时效校验
            # cls.token_time[secret]=datetime.now()
        return cls.token[secret]

    @classmethod
    def get_access_token(cls,secret):
        r=requests.get(cls.token_url,
                        params={'corpid':cls.corpid,'corpsecret':secret})
        print(cls.format(r))
        assert r.json()["errcode"]==0
        return r.json()

    