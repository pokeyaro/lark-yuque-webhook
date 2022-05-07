# -*- coding: UTF-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import BASE_PATH
import json

json_filepath = os.path.join(BASE_PATH, 'meg_card', 'files', 'assistant_card.json')


def __assistant_card() -> dict:
    cards = {
        "config": {
            "wide_screen_mode": True
        },
        "header": {
            "template": "purple",
            "title": {
                "content": "🪶 语雀 - 让再小的个体，也拥有自己的数字花园 ☘️",
                "tag": "plain_text"
            }
        },
        "elements": [{
            "extra": {
                "alt": {
                    "content": "",
                    "tag": "plain_text"
                },
                "img_key": "img_v2_d24d654b-21cb-4858-9edf-1ff1e927dd9g",
                "tag": "img"
            },
            "tag": "div",
            "text": {
                "content": "🌀  语雀，🐜 旗下的在线文档编辑与协同工具。\n🌀  语雀小助手，又名 “小雀同学”。小雀诞生很神奇 🐣 连薅三家大厂羊毛，有生之年系列 BAT 联创出品（头条 *Lark Bot*, 阿里 *YuQue*, 腾讯 *Cloud Infra* 服务）。",
                "tag": "lark_md"
            }
        }, {
            "alt": {
                "content": "",
                "tag": "plain_text"
            },
            "img_key": "img_v2_aab78eaf-51bc-4f62-9ea5-8c521c2150ag",
            "tag": "img"
        }, {
            "fields": [{
                "is_short": True,
                "text": {
                    "content": "**中文学名：**\n[语雀](https://www.yuque.com/about/careers)",
                    "tag": "lark_md"
                }
            }, {
                "is_short": True,
                "text": {
                    "content": "**英文名称：**\n[Yu Que](https://www.yuque.com/about/)",
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
                    "content": "**「语」💬：**\n[人与人高效的沟通方式](https://baike.baidu.com/item/%E8%AF%AD%E9%9B%80/24190957?fr=aladdin)",
                    "tag": "lark_md"
                }
            }, {
                "is_short": True,
                "text": {
                    "content": "**☁️「雀」：**\n[象征 “欢乐、光明、美丽”，轻灵美观](https://baike.baidu.com/item/%E8%AF%AD%E9%9B%80/24190957?fr=aladdin)",
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
                    "content": "**APP 应用：**[@小雀同学 (v1.0.0)](https://github.com/PokeyBoa/lark_yuque_webhook)",
                    "tag": "lark_md"
                }
            }],
            "tag": "div"
        }, {
            "tag": "hr"
        }, {
            "extra": {
                "alt": {
                    "content": "",
                    "tag": "plain_text"
                },
                "img_key": "img_v2_03706b68-884d-415a-9552-0361849b210g",
                "tag": "img"
            },
            "tag": "div",
            "text": {
                "content": "**助手名片**\n\n🔸 **应用：**Yuque Assistant\t\t\t       🔹 **爱好：**@小雀同学 陪唠嗑\n🔸 **名片：**'/help' or call my name\t\t       🔹 **能力：**Wiki 库更新 ➡️ 飞书群组\n",
                "tag": "lark_md"
            }
        }, {
            "tag": "hr"
        }, {
            "fields": [{
                "is_short": False,
                "text": {
                    "content": "**Repo Webhook**",
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
                    "content": "[发布内容 ✅](https://open.feishu.cn)",
                    "tag": "lark_md"
                }
            }, {
                "is_short": True,
                "text": {
                    "content": "[更新内容 ✅](https://open.feishu.cn)",
                    "tag": "lark_md"
                }
            }, {
                "is_short": True,
                "text": {
                    "content": "[发表评论 ✅](https://open.feishu.cn)",
                    "tag": "lark_md"
                }
            }, {
                "is_short": True,
                "text": {
                    "content": "[更新评论 ✅](https://open.feishu.cn)",
                    "tag": "lark_md"
                }
            }, {
                "is_short": True,
                "text": {
                    "content": "[回复评论 ✅](https://open.feishu.cn)",
                    "tag": "lark_md"
                }
            }, {
                "is_short": True,
                "text": {
                    "content": "[评审功能 ⛔](https://open.feishu.cn)",
                    "tag": "lark_md"
                }
            }],
            "tag": "div"
        }, {
            "tag": "hr"
        }, {
            "elements": [{
                "alt": {
                    "content": "",
                    "tag": "plain_text"
                },
                "img_key": "img_v2_ce77be32-d666-4488-89e8-9b7ca4991b0g",
                "tag": "img"
            }, {
                "content": "以上部分内容摘自 Baidu 百科词条",
                "tag": "plain_text"
            }],
            "tag": "note"
        }]
    }
    return cards


def __save_file() -> None:
    res = __assistant_card()
    with open(json_filepath, mode='w', encoding='utf-8') as f:
        json.dump(res, f)
    print(res)


def rjson() -> dict:
    with open(json_filepath, mode='rt', encoding='utf-8') as f:                                                                                                                                                              
        content = json.load(f)
    return content


if __name__ == '__main__':
    # __save_file()
    res = rjson()
    print(res)

