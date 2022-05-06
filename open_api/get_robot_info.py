# -*- coding: UTF-8 -*-
# import os, sys; sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import requests
from open_api.auth_headers import access_token

def get_app_info() -> dict:
    """
    Get the app info.
    """
    data = {}
    headers = access_token()
    if not headers:
        return data
    url = "https://open.feishu.cn/open-apis/bot/v3/info"
    response = requests.request(method="GET", url=url, headers=headers)
    if response.status_code == 200:
        robot = response.json().get('bot')
        if robot.get('activate_status') == 2:
            data = {
                'app_name': robot.get('app_name'),
                'open_id': robot.get('open_id')
            }
    return data


if __name__ == '__main__':
    res = get_app_info()
    print(res)

