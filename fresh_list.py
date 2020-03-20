"""
同学圈动态接口
"""

import requests

import config

cookies = config.cookies
headers = config.headers

params = (
    ('limits', '20'),
    ('timeValue', ''),
)

response = requests.get(
    url='https://www.cpdaily.com/v3/circle/freshList/defaultCircle',
    headers=headers,
    cookies=cookies
)

print(response.text)
