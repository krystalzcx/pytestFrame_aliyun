import requests
import yaml
import logging

class Weixin:
    logging.basicConfig(level=logging.INFO,
                    # filename='new.log',
                    # filemode='a',
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s' )
    log = logging.getLogger("weixin")

    _token=""

    @classmethod
    def get_token(cls):

        if len(cls._token)==0:
            cls._token=cls.get_token_news()
        return cls._token

    @classmethod
    def get_token_news(cls):
        conf=yaml.safe_load(open("contact/weixin.yaml"))
        #logging.debug(conf["env"])
        # cls.log.debug(conf["env"])
        r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                        params={"corpid":conf["env"]["corp_id"],"corpsecret":conf["env"]["secret"]}).json()
        return r["access_token"]
        
            