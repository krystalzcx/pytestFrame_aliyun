import sys
import os
from jsonpath import jsonpath
sys.path.append(os.getcwd())
from api.tag import Tag
from api.base_api import BaseApi
import pytest


class TestTag:
    data=BaseApi.yaml_load("/root/myworkspace/pytestFrame_aliyun/wework/testcase/test_tag.data.yaml")

    @classmethod
    def setup_class(cls):
        cls.tag=Tag()
        #遍历删除测试数据
        cls.reset()
       


    def test_get(self):
        r=self.tag.get()
        assert r['errcode']==0
        # print("tag 打印")
        # print(jsonpath(r,"$..tag[?(@.name=='demo3')]")[0]["id"])

    
    def test_add(self):
        r=self.tag.add('demo_1')
        assert r['errcode']==0

    #此用例有问题，始终返回41017
    # @pytest.mark.parametrize("name",[
    #     "demo1","中文","123"," ","*","😊",""
    # ])
    # data["test_delete"]取的是yaml文件中的key-value
    @pytest.mark.parametrize("name",data["test_delete"])
    def test_delete(self,name):
        # name='demo3'
        r=self.tag.get()
        #如果有就删除
        x=self.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")
        #避免len(x)=0的情况：isinstance(x,list) 判断是否是列表
        if isinstance(x,list) and len(x)>0:
            tag_id=x[0]["id"]
            r=self.tag.delete(tag_id=[tag_id])
            
                   
        #环境干净后开始测试
        #1.先查询
        r=self.tag.get()
        x=self.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")
        path="$..tag[?(@.name!='')]"
        size=len(self.tag.jsonpath(path))
        #2.再增加
        self.tag.add(name)
        #3.在查询
        r=self.tag.get()
        #判断长度增加
        assert len(self.tag.jsonpath(path)) == (size+1)
        tag_id=self.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")[0]['id']
        #4.删除
        r=self.tag.delete(tag_id=[tag_id])
        assert r['errcode']==0
        #5.最后查询，断言
        r=self.tag.get()
        assert len(self.tag.jsonpath(path)) == size


        
    # #setup比teardown稳定
    # def setup(self):
    #     self.reset()

    # def teardown(self):
    #     #在用例执行被强行kill的时候，teardown有可能会得不到执行
    #     self.reset()

    @classmethod
    def reset(cls):
        cls.tag.get()
        #删除测试组
        #遍历删除测试数据
        for name in ["demo1","demo2"]:
            x=cls.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")
            #避免len(x)=0的情况：isinstance(x,list) 判断是否是列表
            if isinstance(x,list) and len(x)>0:
                tag_id=x[0]["id"]
                r=cls.tag.delete(tag_id=[tag_id])

