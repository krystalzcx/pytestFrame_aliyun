import requests
import json
from jsonpath import jsonpath

class TestDemo:
    def test_json(self):
        r=requests.get("https://ceshiren.com/categories.json")
        print(json.dumps(json.loads(r.text),indent=2,ensure_ascii=False))
        assert r.status_code==200
        #断言name='开源项目'对应的description字段的值是否是'开源项目交流与维护'
        # for item in r.json()["category_list"]["categories"]:
        #     if item["name"]=='开源项目':
        #         break
        # print(item)
        # assert item["description"]=='开源项目交流与维护'
        # 找打所有的name的key对应的value
        # print(jsonpath(r.json(),'$..name')
        # """
        # $..categories：取出所有categories对应值
        # []迭代器
        # ?()过滤操作
        # @现行节点
        # [?(@.name=='开源项目')]循环搜索name='开源项目'的节点
        # [0]取出本身
        # """
        assert jsonpath(r.json(),'$..categories[?(@.name=="开源项目")]')[0]['description']=='开源项目交流与维护'