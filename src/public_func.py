# -*- coding: UTF-8 -*-
# import os, sys; sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.settings import NICK_NAME
import random


def empty_dialogue() -> str:
    choose_reply = ['干嘛, 没空陪你撩闲! 你待一边活泥巴去吧!', 
                    '这是表达个锤子? 艾特不说话, 等于耍流氓!', 
                    '心情好, 告诉你个秘密, 想要寻求帮助: /help',
                    '我在赚我的小目标, 十个亿以下的项目不要打扰我!',
                    f'礼貌点呦, 呼叫 \'{NICK_NAME}\', 看见会回复的!']
    res = random.choice(choose_reply)
    return res


def bot_msg_talking(content: dict, flag: int = 1) -> dict:
    """
    flag: 1 means 'p2p' (default)
          0 means 'group'
    """
    if not content:
        data = {'text': '风太大, 我听不清呀!'}
    else:
        data = {}
        info = content.get('text')
        if not info:
            data = {'text': '人类迷惑行为大赏, 愣是给我整不会了...'}
        else:
            if flag == 1:
                # 情景0
                data = {'text': "你在讲啥子呦?"}

                # 情景1
                keyworks1 = ['hhh', 'hehe', '呵呵']
                for i in keyworks1:
                    if i in info:
                        data = {'text': '呵呵你大爷!\n挨劳资一锤?'}
                        break

                # 情景2
                keyworks2 = ['在搞啥', '干啥呢', '干嘛呢', '在干嘛', '在干啥', '干啥子', '搞啥呢', '做什么', '搞什么', '干什么', '闲着么']
                for i in keyworks2:
                    if i in info:
                        data = {'text': '刷抖音!'}
                        break

                # 情景3
                keyworks3 = ['ha', 'o', 'en', '嗯', '哦', '啊', '呃', '额', '哈', '好', '是', '行']
                for i in keyworks3:
                    if (info in i*3) or (i in info):
                        data = {'text': f'{NICK_NAME}已阅。'}
                        break

                # 情景4
                keyworks4 = ['hello', 'hi', '你好']
                for i in keyworks4:
                    if i in info.lower():
                        data = {'text': 'Hi Bro ~\n使用 /help 来唤醒我呀!'}
                        break

            elif flag == 0:
                if info == "/help" or info == NICK_NAME:
                    # 需要使用卡片
                    data = {'text': '叫我干甚?'}
    return data


if __name__ == '__main__':
    bot_msg_talking({})

