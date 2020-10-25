# -*- coding:utf-8 -*-
# Author:Queen_XTT
import json, os
from urllib.parse import urlencode
from urllib.request import urlopen
from common.log import Log

log = Log()
pyname = os.path.basename(__file__)
url = 'http://api.k780.com'
appkey = 10003
sign = "b59bc3ef6191eb9f747dd4e83c99f2a4"


def get_local_ip():
    log.info("[ {} ------ get_local_ip ------ start ]".format(pyname))
    params = {
        'app': 'ip.local',
        'appkey': appkey,
        'sign': sign,
        'format': 'json',
    }
    params = urlencode(params)

    f = urlopen('%s?%s' % (url, params))
    nowapi_call = f.read()
    # print content
    a_result = json.loads(nowapi_call)
    content = ""
    if a_result:
        if a_result['success'] != '0':
            content = a_result['result']
        else:
            content = a_result['msgid'] + ' ' + a_result['msg']
    else:
        print('Request nowapi fail.')
    # print(content)
    log.info("[ {} ------ get_local_ip ------ end ]\n".format(pyname))
    return content


if __name__ == '__main__':
    get_local_ip()
