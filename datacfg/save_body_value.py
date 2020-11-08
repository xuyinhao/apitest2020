"""
保存响应体中，需要保存的值
"""
from datacfg.get_conf import GetConf
from utils.common_util import CommonUtil
import traceback
import json
from base.LogUtil import my_log
log=my_log(__file__)


class SaveBodyValue():
    KEY_ERROR_RET = "NOF_FOUND_KEY"

    '''
    从响应体中，保存需要被保存的变量到conf.ini文件里
    '''

    def __init__(self):
        self.getconf = GetConf()
        self.comtool=CommonUtil()

    def save_value_to_conf(self, get_body_value, current_result):
        '''
        从json文件中，提取值，最终返回字典
        :param save_body_value: 传递一个字典（“user":"data[0].name"
        :param current_result:  需要从该内容中 匹配提取
        :return:  dictvalue  "user":"admin"
        '''
        current_result = current_result     #所有内容
        dictvalue = {}
        if not isinstance(current_result, dict):
            try:
                current_result = json.loads(current_result)
            except Exception as e :
                traceback.print_exc()
                return None
        if not isinstance(get_body_value, dict):
            try:
                get_body_value = json.loads(get_body_value)
            except Exception as e :
                traceback.print_exc()
                return None

        for keyname in dict(get_body_value):
            save_key=keyname
            get_save_value_jmespath = get_body_value[save_key]
            save_value=self.comtool.json_search(get_save_value_jmespath,current_result)
            dictvalue[save_key]=save_value
            print("保存的k,v:",save_key,save_value)
            if not self.getconf.write_conf_value(save_key,save_value):
                return False
        return True


if __name__ == '__main__':
    sbv = SaveBodyValue()
    a={
  "code": 200,
  "data": {
    "current": 1,
    "hitCount": "false",
    "optimizeCountSql": "true",
    "orders": [],
    "pages": 2,
    "records": [
      {
        "accountType": 0,
        "company": "",
        "coreOrganizations": [
          {
            "createTime": "2020-11-06T07:35:21.000+0000",
            "fullName": "深组织name全称",
            "id": 337,
            "orgDesc": "深组织name全称备注",
            "orgDistinguishedName": "",
            "orgName": "深组织name",
            "parentId": 0,
            "sourceId": "",
            "sourceType": 0,
            "systemId": 1,
            "updateTime": "2020-11-06T07:35:21.000+0000"
          }
        ],
        "createTime": "2020-11-06T07:38:18.000+0000",
        "creator": 23,
        "email": "jj@qq.cc",
        "id": 28,
        "isManager": 0,
        "login": "jj1",
        "mender": 0,
        "name": "jjjjj",
        "phone": "",
        "source": 0,
        "state": 0,
        "updateTime": "2020-11-06T07:38:18.000+0000"
      },
      {
        "accountType": 0,
        "company": "",
        "coreOrganizations": [
          {
            "createTime": "2020-11-03T03:42:22.000+0000",
            "fullName": "二级组织1",
            "id": 334,
            "orgDesc": "二级组织1",
            "orgDistinguishedName": "",
            "orgName": "二级组织1",
            "parentId": 330,
            "sourceId": "",
            "sourceType": 0,
            "systemId": 1,
            "updateTime": "2020-11-03T03:42:22.000+0000"
          }
        ],
        "createTime": "2020-11-06T06:09:37.000+0000",
        "creator": 1,
        "email": "tpf-06@user.com",
        "id": 27,
        "isManager": 0,
        "login": "tpf-06",
        "mender": 0,
        "name": "tpf-06",
        "phone": "17745487545",
        "source": 0,
        "state": 0,
        "updateTime": "2020-11-07T05:37:16.000+0000"
      },
      {
        "accountType": 0,
        "company": "",
        "coreOrganizations": [
          {
            "createTime": "2020-11-03T03:42:50.000+0000",
            "fullName": "三级组织1",
            "id": 336,
            "orgDesc": "三级组织1",
            "orgDistinguishedName": "",
            "orgName": "三级组织1",
            "parentId": 334,
            "sourceId": "",
            "sourceType": 0,
            "systemId": 1,
            "updateTime": "2020-11-03T03:42:50.000+0000"
          }
        ],
        "createTime": "2020-11-06T01:40:39.000+0000",
        "creator": 1,
        "email": "tpf-05@user.com",
        "id": 26,
        "isManager": 0,
        "login": "tpf-05",
        "mender": 26,
        "name": "tpf-05",
        "phone": "17787878586",
        "source": 0,
        "state": 0,
        "updateTime": "2020-11-06T06:59:33.000+0000"
      },
      {
        "accountType": 0,
        "company": "",
        "coreOrganizations": [
          {
            "createTime": "2020-11-06T07:42:00.000+0000",
            "fullName": "z组织组织组织组织组织组织全名08",
            "id": 362,
            "orgDesc": "z组织组织组织组织组织组织test 描述08",
            "orgDistinguishedName": "",
            "orgName": "z组织组织组织组织组织08",
            "parentId": 361,
            "sourceId": "",
            "sourceType": 0,
            "systemId": 1,
            "updateTime": "2020-11-06T07:42:00.000+0000"
          }
        ],
        "createTime": "2020-11-03T05:35:58.000+0000",
        "creator": 23,
        "email": "u@youx.cc",
        "id": 25,
        "isManager": 0,
        "login": "user2",
        "mender": 25,
        "name": "user2用户名",
        "phone": "",
        "source": 0,
        "state": 0,
        "updateTime": "2020-11-06T08:02:56.000+0000"
      },
      {
        "accountType": 0,
        "company": "",
        "coreOrganizations": [
          {
            "createTime": "2020-11-03T01:07:42.000+0000",
            "fullName": "开发四部",
            "id": 333,
            "orgDesc": "",
            "orgDistinguishedName": "",
            "orgName": "开发四部",
            "parentId": 332,
            "sourceId": "",
            "sourceType": 0,
            "systemId": 1,
            "updateTime": "2020-11-03T01:07:42.000+0000"
          }
        ],
        "createTime": "2020-11-03T01:10:32.000+0000",
        "creator": 1,
        "email": "Jason@163.com",
        "id": 24,
        "isManager": 0,
        "login": "Jason",
        "mender": 24,
        "name": "Jason",
        "phone": "",
        "source": 0,
        "state": 0,
        "updateTime": "2020-11-07T09:08:01.000+0000"
      },
      {
        "accountType": 0,
        "company": "",
        "coreOrganizations": [
          {
            "createTime": "2020-11-02T11:45:34.000+0000",
            "fullName": "测试组织_啊1-1 全称",
            "id": 329,
            "orgDesc": " 测试组织_啊1 备注",
            "orgDistinguishedName": "",
            "orgName": "测试组织_啊1-1",
            "parentId": 328,
            "sourceId": "",
            "sourceType": 0,
            "systemId": 1,
            "updateTime": "2020-11-02T11:45:34.000+0000"
          }
        ],
        "createTime": "2020-11-02T11:52:55.000+0000",
        "creator": 1,
        "email": "user@u.cc",
        "id": 23,
        "isManager": 0,
        "login": "user1",
        "mender": 0,
        "name": "user1",
        "phone": "",
        "source": 0,
        "state": 0,
        "updateTime": "2020-11-08T02:06:39.000+0000"
      },
      {
        "accountType": 0,
        "company": "",
        "coreOrganizations": [
          {
            "createTime": "2020-11-03T03:42:50.000+0000",
            "fullName": "三级组织1",
            "id": 336,
            "orgDesc": "三级组织1",
            "orgDistinguishedName": "",
            "orgName": "三级组织1",
            "parentId": 334,
            "sourceId": "",
            "sourceType": 0,
            "systemId": 1,
            "updateTime": "2020-11-03T03:42:50.000+0000"
          }
        ],
        "createTime": "2020-11-02T11:46:51.000+0000",
        "creator": 1,
        "email": "tpf-04@user.com",
        "id": 22,
        "isManager": 0,
        "login": "tpf-04",
        "mender": 0,
        "name": "tpf-04",
        "phone": "14545874561",
        "source": 0,
        "state": 0,
        "updateTime": "2020-11-06T03:34:29.000+0000"
      },
      {
        "accountType": 0,
        "company": "",
        "coreOrganizations": [
          {
            "createTime": "2020-11-03T03:42:34.000+0000",
            "fullName": "二级组织2",
            "id": 335,
            "orgDesc": "二级组织2",
            "orgDistinguishedName": "",
            "orgName": "二级组织2",
            "parentId": 330,
            "sourceId": "",
            "sourceType": 0,
            "systemId": 1,
            "updateTime": "2020-11-03T03:42:34.000+0000"
          }
        ],
        "createTime": "2020-11-02T11:46:16.000+0000",
        "creator": 1,
        "email": "tpf-03@user.com",
        "id": 21,
        "isManager": 0,
        "login": "tpf-03",
        "mender": 0,
        "name": "tpf-03",
        "phone": "14545874561",
        "source": 0,
        "state": 0,
        "updateTime": "2020-11-07T05:00:12.000+0000"
      },
      {
        "accountType": 0,
        "company": "",
        "coreOrganizations": [
          {
            "createTime": "2020-11-03T03:42:22.000+0000",
            "fullName": "二级组织1",
            "id": 334,
            "orgDesc": "二级组织1",
            "orgDistinguishedName": "",
            "orgName": "二级组织1",
            "parentId": 330,
            "sourceId": "",
            "sourceType": 0,
            "systemId": 1,
            "updateTime": "2020-11-03T03:42:22.000+0000"
          }
        ],
        "createTime": "2020-11-02T11:45:46.000+0000",
        "creator": 1,
        "email": "tpf-02@user.com",
        "id": 20,
        "isManager": 0,
        "login": "tpf-02",
        "mender": 20,
        "name": "tpf-02",
        "phone": "14545874561",
        "source": 0,
        "state": 0,
        "updateTime": "2020-11-04T02:39:34.000+0000"
      },
      {
        "accountType": 0,
        "company": "",
        "coreOrganizations": [],
        "createTime": "2020-11-02T11:44:50.000+0000",
        "creator": 1,
        "email": "x@qqqq.cc",
        "id": 19,
        "isManager": 0,
        "login": "xadmin",
        "mender": 0,
        "name": "xadmin用户",
        "phone": "",
        "source": 0,
        "state": 1,
        "updateTime": "2020-11-07T15:54:27.000+0000"
      }
    ],
    "searchCount": "true",
    "size": 10,
    "total": 16
  },
  "entity": "null",
  "exceptionStackTrace": "null",
  "message": "null",
  "state": "success"
}
    value = '{"user1":"data.records[0].name","user2":"data.records[1].name"}'
    current_result = a
    print(sbv.save_value_to_conf(value, current_result))