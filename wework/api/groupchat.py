import requests
import json
from api.wework_token import WeWork


class GroupChat(WeWork):
    # 继承类WeWork，子类有与父类同名变量，子类的变量值会覆盖父类
    secret='g6HTdjCLPYqGL54RtfbIn1oGZcKw9SOehw9CaH1XelM'
    token=WeWork.get_token(secret)

    def list(self,offset=0,limit=1000,**kwargs):
        json_data={'offset':offset,'limit':limit}
        #为了适应json里有更多参数的场景
        json_data.update(kwargs)
        url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list'
        r=requests.post(url,
                        params={'access_token':self.token}, #params={'access_token':self.get_token(self.secret)}
                        json=json_data)
        #todo:自动加解密
        #todo:多环境支持，根据配置可以一套case测试多套环境，需要修改host
        return r.json()

    def get(self,chat_id):
        detail_url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/get'
        r=requests.post(detail_url,
                        params={'access_token':self.token},
                        json={'chat_id':chat_id})
        # print(json.dumps(r.json,indent=2))
        return r.json()