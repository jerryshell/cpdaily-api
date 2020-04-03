import encoder

# 打开你手机的 /storage/emulated/0/wismcp/device/device_id.json 文件，将 deviceId 的值填入 device_id 变量中，deviceId 应该是一个 UUID
device_id = ''

cpdaily_info = '{"systemName":"android","systemVersion":"6.0.1","model":"V9","deviceId":"' + device_id + '","appVersion":"8.0.8","lon":0,"lat":0,"userId":""}'

print('请将以下编码后的设备信息填入 config.py 的 cpdaily_info 变量中')
print(encoder.encode(cpdaily_info))
