# -*- coding: UTF-8 -*-

def forward_news(**kwargs) -> dict:
    cards = {
        "config": {
            "wide_screen_mode": True
        },
        "header": {
            "template": "green",
            "title": {
                "content": "🪶 小雀温馨提醒：收到一条来自 BAT 的消息推送",
                "tag": "plain_text"
            }
        },
        "elements": [{
            "fields": [{
                "is_short": True,
                "text": {
                    "content": "**☘️ 响应侧：**\n     @ALL",
                    "tag": "lark_md"
                }
            }, {
                "is_short": True,
                "text": {
                    "content": f"**🔥 事件类型：**\n     {kwargs['hook_type']}",
                    "tag": "lark_md"
                }
            }, {
                "is_short": False,
                "text": {
                    "content": "",
                    "tag": "lark_md"
                }
            }, {
                "is_short": True,
                "text": {
                    "content": "**📲 事件来源：**\n     YuQue Webhook",
                    "tag": "lark_md"
                }
            }, {
                "is_short": True,
                "text": {
                    "content": f"**📘 事件描述：**\n     [{kwargs['title_name']}]({kwargs['file_url']})",
                    "tag": "lark_md"
                }
            }, {
                "is_short": False,
                "text": {
                    "content": "",
                    "tag": "lark_md"
                }
            }, {
                "is_short": True,
                "text": {
                    "content": f"**🌎 更新时间：**\n     {kwargs['update_time']}",
                    "tag": "lark_md"
                }
            }],
            "tag": "div"
        }, {
            "tag": "hr"
        }, {
            "actions": [{
                "tag": "button",
                "text": {
                    "content": "🥶 吃瓜",
                    "tag": "lark_md"
                },
                "value": {
                    "button_type": "common",
                    "button_id": "bd_132529342258964",
                },
                "type": "default"
            }, {
                "tag": "button",
                "text": {
                    "content": "👍 炒鸡",
                    "tag": "lark_md"
                },
                "value": {
                    "button_type": "great",
                    "button_id": "bd_132529342258964",
                },
                "type": "primary"
            }, {
                "tag": "button",
                "text": {
                    "content": "🥳 爆赞",
                    "tag": "lark_md"
                },
                "value": {
                    "button_type": "perfect",
                    "button_id": "bd_132529342258964",
                },
                "type": "danger"
            }],
            "tag": "action"
        }, {
            "tag": "hr"
        }, {
            "elements": [{
                "alt": {
                    "content": "",
                    "tag": "plain_text"
                },
                "img_key": "img_v2_508b657d-5903-437a-a5b2-1686d9698deg",
                "tag": "img"
            }, {
                "content": f"小雀同学: 来自 '{kwargs['group_name']}' 的各位好，如有其它疑问，请告诉万能的 @头条爸爸 (toutiao.com)",
                "tag": "plain_text"
            }],
            "tag": "note"
        }]
    }
    return cards


if __name__ == '__main__':
    data = {
        "hook_type": "内容发布（初版）",
        "title_name": "百度知道《疫情啥时候结束》",
        "file_url": "www.baidu.com",
        "update_time": "北京时间 [2021-05-25 17:21:14]",
        "group_name": "油茶麻花团队"
    }
    res = forward_news(**data)
    print(res)

