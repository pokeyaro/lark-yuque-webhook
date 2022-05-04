# -*- coding: UTF-8 -*-
"""
加密方式
事件内容采用AES-256-CBC加密，加密过程：

使用SHA256对EncryptKey进行哈希得到密钥key；
使用PKCS7Padding方式将事件内容进行填充；
生成16个字节的随机数作为初始向量iv；
使用iv和key对事件内容加密得到encryped_event；
应用收到的密文encrypt为base64(iv+encryped_event)。
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import hashlib
import base64
import json
from Crypto.Cipher import AES
from settings import ENCRYPT_KEY

class AESCipher(object):
    def __init__(self, key):
        self.bs = AES.block_size
        self.key=hashlib.sha256(AESCipher.str_to_bytes(key)).digest()

    @staticmethod
    def str_to_bytes(data):
        u_type = type(b"".decode('utf8'))
        if isinstance(data, u_type):
            return data.encode('utf8')
        return data

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]

    def decrypt(self, enc):
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return  self._unpad(cipher.decrypt(enc[AES.block_size:]))

    def decrypt_string(self, enc):
        enc = base64.b64decode(enc)
        return  self.decrypt(enc).decode('utf8')


def parse_event(encrypt: str) -> dict:
    """
    Event decryption, revert to dictionary format.
    """
    cipher = AESCipher(ENCRYPT_KEY)
    decrypt = cipher.decrypt_string(encrypt)
    data = json.loads(decrypt)
    return data


if __name__ == '__main__':
    encrypt = "P37w+VZImNgPEO1RBhJ6RtKl7n6zymIbEG1pReEzghk="
    data = parse_event(encrypt)
    print(data)

