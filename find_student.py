"""
同学列表接口
"""

import requests

import config

cookies = config.cookies
headers = config.headers

params = (
    ('limits', '20'),
    ('offset', '0'),
)

response = requests.get(
    url='https://www.cpdaily.com/v6/user/findStudent',
    headers=headers,
    params=params,
    cookies=cookies
)

print(response.text)
