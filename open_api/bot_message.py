# -*- coding: UTF-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
import requests
from open_api.auth_headers import access_token

def reply_meg(msg_id: str, msg_type: str, content: dict) -> bool:
    """
    Robot reply message api.
    """
    headers = access_token()
    if not headers:
        return False
    url = f"https://open.feishu.cn/open-apis/im/v1/messages/{msg_id}/reply"
    payload = json.dumps({
        'content': json.dumps(content),
        'msg_type': msg_type
    })
    response = requests.request(method="POST", url=url, headers=headers, data=payload)
    if response.status_code == 200:
        print(response.json())
        return True
    return False


if __name__ == '__main__':
    data = {
        "msg_id": "om_xxxxxxxxxxxxxx",
        "msg_type": "text",
        "content": {'text': 'hello~'}
    }
    reply_meg(**data)

