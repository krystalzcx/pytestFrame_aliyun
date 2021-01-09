import requests
import json
import sys
import os 
sys.path.append(os.getcwd())
print(sys.path)
from api.groupchat import  GroupChat
from  api.wework_token import WeWork

class TestGroupChat:
    
    #成员变量
    token=None
    @classmethod
    def setup_class(cls):
        #封装接口类实例化
        cls.groupchat=GroupChat()
        #类方法可以直接使用类名引用
        #这个模块中对应secret是在封装模块接口类GroupChat就定好了的
        # cls.token=WeWork.get_token(cls.groupchat.secret)

    def test_groupchat_get(self):
        r=self.groupchat.list()
        assert r['errcode']==0

    def test_groupchat_get_status(self):
        r=self.groupchat.list(status_filter=1)
        assert r['errcode']==0
    
    
    def test_groupchat_detail(self):
        r=self.groupchat.list()
        chat_id=r["group_chat_list"][0]['chat_id']
        r=self.groupchat.get(chat_id)
        assert r['errcode']==0
        assert len(r['group_chat']['member_list']) > 0
        