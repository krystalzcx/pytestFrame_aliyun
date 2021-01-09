import pytest
from  contact.token import Weixin

#本次执行，只会保存一次(运行一次)
@pytest.fixture(scope="session")
def token():
    return Weixin.get_token_news()