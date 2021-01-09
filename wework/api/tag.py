from api.wework_token import WeWork
import json
import requests

class Tag(WeWork):
    #secret='g6HTdjCLPYqGL54RtfbIn1oGZcKw9SOehw9CaH1XelM'
    def get(self):
        url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list'
        r=requests.post(
            url,
            params={'access_token':self.get_token(self.secret)},
            json={"tag_id":[]}
        )
        self.format(r)
        return r.json()

    def add(self,name,**kwargs):
        url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag'
        r=requests.post(
            url,
            params={'access_token':self.get_token(self.secret)},
            json={
                "group_id": "etLl_hDAAAklvXqANTVGVSfpn_n9sZ9w",
                "tag":[{"name":name}]
                }
        )
        # self.format(r)
        return r.json()


    def update(self):
        pass
     
    def delete(self,tag_id=[],group_id=[]):
        url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag'
        r=requests.post(
            url,
            params={'access_token':self.get_token(self.secret)},
            json={
                "tag":tag_id,
                "group_id":group_id
                }
            
        )
        self.format(r)
        return r.json()