import pystache
import time

#一些公共方法
class Utils:
    #读取文件，并替换模板中的变量
    #由读取请求json文件，使用mustache(pystache)技术，动态改变参数演变而来
    @classmethod
    def parse(self,template_path,dict):
        template="".join(open(template_path).readlines())
        return pystache.render(template,dict)

    #取11位不重复的数字
    @classmethod
    def udid(self):
        return str(time.time()).replace(".","")[0:11]