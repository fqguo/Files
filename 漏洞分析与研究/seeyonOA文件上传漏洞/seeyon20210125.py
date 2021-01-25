#!/usr/bin/env python3
#coding=utf-8

import requests
import base64
import json
import re
import sys

def Get_Target():
    querystr = "\"seeyon\" && country=\"CN\" && title=\"北京\""
    enquerystr = (base64.b64encode(querystr.encode())).decode("utf-8")
    print(enquerystr)
    url = "https://fofa.so/api/v1/search/all?email=xxxx@qq.com&key=xxx&qbase64="+enquerystr+"&size=200"
    resp = requests.get(url)
    json_dict = json.loads(resp.text)
    list1 = []

    for results in json_dict["results"]: #根据返回的json数据获取results
        result = json.dumps(results)        #去掉u字符，字典数据转成字符串
        res = re.findall(r"\[\"(.+?)\"\,", result)
        try:
            resp1 = requests.get("http://"+res[0], timeout=3, verify=False)
            if resp1.status_code == 200:
                list1.append(res[0])       #存入列表
        except Exception as e:
            pass

    list1 = list(set(list1))   #去重

    for lis in list1:
        try:
            with open ("seeyon20210125.txt", "a") as f:
                lis = "http://" + lis
                f.write(lis+"\n")
        except Exception as e:
            pass


if __name__ == "__main__":
    Get_Target()
