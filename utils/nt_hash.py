# -*- coding: UTF-8 -*-
from passlib.hash import nthash

def nt(data: str) -> str:
    if type(data) != str:
        data = str(data)
    htlm_str = nthash.hash(data)
    return htlm_str

if __name__ == '__main__':
    info = "hello world"
    data = nt(info)
    print(data)

