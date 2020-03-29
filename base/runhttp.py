try:
    import requests
    import json
except:
    print("Import error")

class RunMethod():
    # def __init__(self,method,url,data=None):
    #     self.method=method
    #     self.url = url
    #     self.data = data
    #get请求的 请求
    def _send_get(self,url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url, params=data, headers=header)
        else:
            res = requests.get(url, params=data)
        # print(res.content)
        try:
            res_to_list = [res.status_code, json.dumps(res.json(), indent=2, sort_keys=True, ensure_ascii=False)]
            return res_to_list
        except:
            # return [res.status_code,res.content]
            return [res.status_code,res.content]


    ''' post 请求
        return list  [response_code,response_data]
    '''
    def _send_post(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.post(url, data=data, headers=header)
        else:
            res = requests.post(url, data=data)
        try:
            res_to_list = [res.status_code, json.dumps(res.json(), indent=2, sort_keys=True, ensure_ascii=False)]
            return res_to_list
        except:
            return [res.status_code, res.content]

    #返回日志
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

    def run_main(self, method, url, data=None, header=None):
        if method.lower() == 'get':
            r = self._send_get(url, data, header)
        elif method.lower() == 'post':
            r = self._send_post(url, data, header)
        else:
            return self.log_code(1, 10001, 'Error Method,not get or post!')
        # return json.dumps(r,indent=2,sort_keys=True,ensure_ascii=False)
        return r


if __name__ == '__main__':
    login_url = 'http://127.0.0.1:8000/test01'
    # data = {'username': '1xyh中文', 'mobile': '123456'}
    # data="username=xyh"
    data = {"startdevid": 1,"num":2}
    res = RunMethod()
    res = res.run_main('post', login_url, data)
    print(res)
