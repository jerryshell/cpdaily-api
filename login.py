import requests
from bs4 import BeautifulSoup

import config
import encoder

session = requests.session()

"""
阶段 1：获取 lt
"""

headers = {
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; V9 Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36',
    'cpdailyauthtype': 'Login',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,en-US;q=0.8',
    'X-Requested-With': 'com.wisedu.cpdaily',
}

params = (
    ('service', 'https://www.cpdaily.com/v6/auth/campus/cas/login'),
)

response = session.get(
    url=config.tenant_iap_url + '/login',
    headers=headers,
    params=params
)
lt = BeautifulSoup(response.text, features='html.parser').select_one('#lt')['value']
print('---lt')
print(lt)

"""
阶段 2：获取 iap
"""

uri_encode_lt = lt.replace(':', '%3A')
print('---uri_encode_lt')
print(uri_encode_lt)

headers = {
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; V9 Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Language': 'zh-CN,en-US;q=0.8',
}

data = 'username=' + config.username + '&password=' + config.password + '&lt=' + uri_encode_lt + '&captcha=&rememberMe=false'

response = session.post(
    url=config.tenant_iap_url + '/doLogin',
    headers=headers,
    data=data
)
print('---response')
print(response.text)

iap = response.text.split('ST-iap')[-1]
iap = iap.replace('"}', '')
iap = 'ST-iap' + iap
print('---iap')
print(iap)

"""
阶段 3：编码 iap，获取 ticket
"""

ticket = encoder.encode(iap)
print('---ticket')
print(ticket)

"""
阶段 4：登录
"""

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; V9 Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 okhttp/3.8.1',
    'deviceType': '1',
    'CpdailyStandAlone': '0',
    'CpdailyInfo': config.cpdaily_info,
    'Cache-Control': 'max-age=0',
    'Content-Type': 'application/json; charset=UTF-8',
    'Host': 'www.cpdaily.com',
}

data = '{"tenantId":"' + config.tenant_id + '","ticket":"' + ticket + '"}'
print('---data')
print(data)

response = session.post(
    'https://www.cpdaily.com/v6/auth/authentication/cloud/login',
    headers=headers,
    data=data
)

print('---response')
print(response.text)

"""
阶段 5：提取 sessionToken
"""

sessionToken = response.text.split('sessionToken":"')[-1]
sessionToken = sessionToken.split('"')[0]
print('---sessionToken')
print(sessionToken)
