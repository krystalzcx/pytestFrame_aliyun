import requests
import time
import logging
import pystache
import json
from  contact.token import Weixin
from  contact.user import User
from contact.utils import Utils


class TestUser:
    department_id=3

    @classmethod
    def setup_class(cls):
        #实例化类User
        cls.user=User()

    def test_create(self):
        uid="krystalz"+str(time.time())
        data={
            "userid":uid,
            "name":uid,
            "department":[self.department_id],
            "email":uid+"@testhome.com"
        }
        # logging.debug(self.token)
        r=self.user.create(data)
        logging.debug(Weixin.get_token())
        logging.debug(r)
        assert r["errcode"]==0
    
    def test_create_by_real(self):
        #因为转换过的data并不是json格式，所以需要使用headers指明一下
        uid='krystal_'+str(time.time())
        mobile=str(time.time()).replace(".","")[0:11]
        #此时的data是str
        data=Utils.parse("contact/user_create.json",{"name":uid,"title":"校长","email":mobile+"@qq.com","mobile":mobile})
        data=data.encode("UTF-8")
        logging.debug(type(data))
        # loads()把str转为字典
        # data=json.loads(data)      
        r=self.user.create(data=data)
        logging.debug(r)
        assert r["errcode"]==0

    #部门下的成员列表
    def test_list(self):
        r=self.user.list()
        logging.debug(r)

        r=self.user.list(3)
        logging.debug(r)


