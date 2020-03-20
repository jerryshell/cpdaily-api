"""
配置文件，请按照顺序依次操作
"""

# 1. 设置登录学号
username = ''
# 2. 设置登录密码
password = ''
# 3. 设置学校 id，这部分可以参考 tenant_list.json，如：华中科技大学设置为 hust
tenant_id = ''
# 4. 设置学校 iap 地址，这部分可以参考 tenant_list.json，如：华中科技大学设置为 http://hust.cpdaily.com/iap
tenant_iap_url = ''

# 5. 现在，请单独执行 login.py

# 6. 请执行 login.py 之后填充 sessionToken
cookies = {
    'sessionToken': '',
}

# 非登录接口的统一 headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; V9 Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 okhttp/3.8.1',
    'Cache-Control': 'max-age=0',
    'Host': 'www.cpdaily.com',
}

# TODO 编码之后的设备信息，以后有时间再单独做一个生成工具吧
cpdaily_info = 'RADCSRminiMgqqlqqEeUIlGO1ivakMDZTJtYYN8fwbnuQ2vxpCSovYxvZRVK9xMNAXbfTZP57pkLqJG8XT9C00dZfuDJfe7Y4nBSLxSfxQKmigyLo5lWNPclxWPSDjxOT+6iY8tfm7qZ0nieURI6Ep4nLL+PWkR8/Ijcw38AnEQO9GIxCFGDauV9QnRGsffcfaSxvLpOHCaWHartZponA5ixvv0rxTf/'
