"""
同学圈热门动态接口
"""

import requests

import config

cookies = config.cookies
headers = config.headers

params = (
    ('talkId', ''),
)

response = requests.get(
    url='https://www.cpdaily.com/v3/content/fresh/hot/freshList',
    headers=headers,
    cookies=cookies
)

print(response.text)
