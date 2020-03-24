import base64

from pyDes import des, CBC, PAD_PKCS5

secret_key = 'XCE927=='
iv = [1, 2, 3, 4, 5, 6, 7, 8]


def encode(s):
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    s_encrypt = k.encrypt(s, padmode=PAD_PKCS5)
    return bytes.decode(base64.b64encode(s_encrypt))


def decode(s):
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    s_decrypt = k.decrypt(base64.b64decode(s), padmode=PAD_PKCS5)
    return bytes.decode(s_decrypt)


if __name__ == '__main__':
    str_encode = encode('ST-iap:1020083955376127:ST:75ffa145-4af5-4a25-8c8e-adf700e94927:20200320233346')
    print(str_encode)
    str_decode = decode(str_encode)
    print(str_decode)
