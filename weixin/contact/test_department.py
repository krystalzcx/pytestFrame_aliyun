#-*- coding:utf-8 -*-
import sys
print(sys.path)
sys.path.append('/root/myworkspace/weixin')
from contact.utils import Utils
from contact.token import Weixin
from contact.department import Department
import requests
import logging
import json 
import datetime
import pytest

class TestDepartment:
    @classmethod
    def setup_class(cls):
        cls.department=Department()

    #参数token是以fixture(conftest.py)来引用的
    def test_create_depth(self):
        parentid=506
        for i in range(5):
            data={
                "name": "2020年11月_"+str(parentid)+str(datetime.datetime.now().timestamp()),
                "parentid": parentid
                }
            # r=requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
            #             params={"access_token":token},
            #             json=data).json()
            r=self.department.create(dict=data)
            logging.debug("第"+str(i)+"循环")
            # logging.debug(Weixin.get_token()) 
            logging.debug(r)
            parentid=r['id']
            assert r["errcode"]==0

    #断言可以根据获取部门列表操作
    def test_create_order(self):
        data={
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
            }
        r=self.department.create(dict=data)
        logging.debug(r)


    #名字需要加后缀，多次执行重复会创建不成功
    @pytest.mark.parametrize("name",[
        "中文-部门_2",
        "English_2"]
    )
    def test_create_name(self,name,token):
        data={
            "name": name+Utils.udid(),
            "parentid": 1
            }
        r=self.department.create(dict=data)
        logging.debug(r)
        assert r["errcode"]==0
    
    def test_get(self,token):
        # logging.debug("token")
        # logging.debug(self.token)
        # logging.debug(TestDepartment.token)
        r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
                params={"access_token": token}).json()
        #格式化结果输出方式
        # logging.info(json.dumps(r,indent=2))

