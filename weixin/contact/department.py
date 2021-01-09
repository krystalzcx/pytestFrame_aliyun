import requests
from contact.token import Weixin

class Department:
    
    def create(self,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                        params={"access_token":Weixin.get_token()},
                        json=dict,
                        data=data).json()
    #部门列表
    #可能参数可以变化
    def list(self):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
                params={"access_token": Weixin.get_token()}).json()