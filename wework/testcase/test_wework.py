import sys
import os 
sys.path.append(os.getcwd())
print(sys.path)
from api.wework_token import WeWork

class TestWeWork:
    
    # @classmethod
    # def setup_class(cls):
    #     cls.token=WeWork.get_token()

    def test_get_token(self):
        r=WeWork.get_access_token(WeWork.secret)
        assert r["errcode"]==0

    