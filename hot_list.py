"""
今日红人榜接口
"""

import requests

import config

cookies = config.cookies
headers = config.headers

params = (
    ('isYesterday', 'false'),
)

response = requests.get(
    url='https://www.cpdaily.com/v3/user/hotList',
    headers=headers,
    params=params,
    cookies=cookies
)

print(response.text)
