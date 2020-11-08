
import requests
import json
from base.LogUtil import my_log
log=my_log(__file__)

class RunMain():
    # def __init__(self,method,url,data=None):
    #     self.method=method
    #     self.url = url
    #     self.data = data
    def send_get(self, url, data=None):
        res = requests.get(url, data=data).json()
        return json.dumps(res, indent=1)

    def send_post(self, url, data=None):
        res = requests.post(url, data=data).json()
        return json.dumps(res, indent=2, sort_keys=True)  # 按照json样式可视化显示

    def log_code(self, level, code, msg):
        r = {}
        if level == 0:
            r['status'] = 'success'
        elif level == 1:
            r['status'] = 'fail'
        else:
            r['status'] = 'warning'
        r['code'] = code
        r['msg'] = msg
        return r

    def run_main(self, method, url, data=None):
        if method == 'GET':
            r = self.send_get(url, data)
        elif method == 'POST':
            r = self.send_post(url, data)
        else:
            return self.log_code(1, 30001, 'Error Method,not get or post!')
        return json.loads(r)


if __name__ == '__main__':
    login_url = 'http://127.0.0.1:8000/login'
    data = {'username': 'xyh', 'password': '123456'}
    res = RunMain()
    res = res.run_main('POST', login_url, data)
    print(res)
