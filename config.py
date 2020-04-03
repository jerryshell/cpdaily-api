"""
配置文件，请按照顺序依次操作
"""

# 1. 设置编码之后的设备信息，使用 cpdaily_info_gen.py 来获得
cpdaily_info = ''

# 2. 设置登录学号
username = ''
# 3. 设置登录密码
password = ''
# 4. 设置学校 id，这部分可以参考 tenant_list.json，如：华中科技大学设置为 hust，注意：有些学校的 id 是一个 uuid，而不是学校英文名
tenant_id = ''
# 5. 设置学校 iap 地址，这部分可以参考 tenant_list.json，如：华中科技大学设置为 http://hust.cpdaily.com/iap
tenant_iap_url = ''

# 6. 现在，请单独执行 login.py

# 7. 请执行 login.py 之后填充 sessionToken
cookies = {
    'sessionToken': '',
}

# 非登录接口的统一 headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; V9 Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 okhttp/3.8.1',
    'Cache-Control': 'max-age=0',
    'Host': 'www.cpdaily.com',
}
