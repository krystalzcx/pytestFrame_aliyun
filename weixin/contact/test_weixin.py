from unittest import TestCase
from contact.token import Weixin


class TestWeixin(TestCase):
    def test_get_token(self):
        # log.debug("test weixin")
        token = Weixin.get_token()
        Weixin.log.info(token)
        assert token != ""
        