# -*- coding: UTF-8 -*-
# import os, sys; sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
import requests
from config.settings import APP_ID, APP_SECRET

def access_token() -> dict:
    """
    Returns the authenticated request header.
    """
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    headers = {
        'Content-Type': 'application/json; charset=utf-8'
    }
    payload = json.dumps({
        'app_id': APP_ID,
        'app_secret': APP_SECRET
    })
    response = requests.request(method="POST", url=url, headers=headers, data=payload)
    result = {}
    if response.status_code == 200:
        token = response.json().get('tenant_access_token')
        result = { 
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json; charset=utf-8'
        }
    return result


if __name__ == '__main__':
    headers = access_token()
    print(headers)

