# -*- coding: UTF-8 -*-
# import os, sys; sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import requests
from open_api.auth_headers import access_token

def get_groups() -> list:
    """
    Get the list of group information where the robot is located.
    """
    data = []
    headers = access_token()
    if not headers:
        return data
    url = "https://open.feishu.cn/open-apis/im/v1/chats"
    query_params = {
        'user_id_type': 'open_id',
        'page_size': 100
    }
    payload = {}
    response = requests.request(
        method="GET",
        url=url,
        params=query_params,
        headers=headers,
        data=payload
    )
    if response.status_code == 200:
        groups = response.json().get('data').get('items')
        for item in groups:
            single = {
                'gname': item.get('name'),
                'gid': item.get('chat_id')
            }
            data.append(single)
    return data


if __name__ == '__main__':
    res = get_groups()
    print(res)

