try:
    import requests
    import json
    from lxml import etree
except:
    print("Import error")

class RunMethod():
    # def __init__(self,method,url,data=None):
    #     self.method=method
    #     self.url = url
    #     self.data = data
    #get请求的 请求

    def _html_trans(self,result):
        result.encoding = 'utf-8'
        html = etree.HTML(result.content)
        html_v = etree.tostring(html,encoding='utf-8').decode('utf-8')
        return  html_v

    def _json_trans(self,result):
        return  json.dumps(result.json(), indent=2, sort_keys=True, ensure_ascii=False)

    def _send_get(self,url, data=None, cookies = None, header=None):
        res = None
        if header != None:
            res = requests.get(url, params=data,cookies = cookies, headers=header)
        else:
            res = requests.get(url, params=data,cookies = cookies)
        # print(res.content)
        # print(requests.utils.dict_from_cookiejar(res.cookies))
        # return res
        try:
            res_to_list = (res.status_code, self._json_trans(res),res)
            return res_to_list
        except:

            html_data = self._html_trans(res)
            return (res.status_code,html_data,res)

        #


    ''' post 请求
        return list  [response_code,response_data]
    '''
    def _send_post(self, url, data=None, cookie = None,header=None):
        res = None
        if header != None:
            res = requests.post(url, data=data, cookies = cookie, headers=header)
        else:
            res = requests.post(url, data=data, cookies = cookie)

        # return res.json()
        try:
            res_to_list = (res.status_code, self._json_trans(res),res)
            return res_to_list
        except:
            html_data = self._html_trans(res)
            return (res.status_code, html_data,res)

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

    def run_main(self, method, url, data=None, cookie = None, header=None):
        if method.lower() == 'get':
            r = self._send_get(url, data, cookie,header)
        elif method.lower() == 'post':
            r = self._send_post(url, data, cookie,header)
        else:
            return self.log_code(1, 10001, 'Error Method,not get or post!')
        # return json.dumps(r,indent=2,sort_keys=True,ensure_ascii=False)
        return r


if __name__ == '__main__':
    login_url = 'http://127.0.0.1:8000/test01'
    # data = {'username': '1xyh中文', 'mobile': '123456'}
    # data="username=xyh"
    # data = {"startdevid": 1,"num":2}
    # res = RunMethod()
    # res = res.run_main('post', login_url, data)
    # print(res)
    url = "https://www.baidu.com"
    res = RunMethod()
    print(res.run_main('get',url))