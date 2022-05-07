# -*- coding: UTF-8 -*-
# import os, sys; sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.settings import NICK_NAME, BASE_PATH
from open_api.bot_message import send_card, send_u_visible_msg, del_u_visible_msg
from open_api.get_group_lists import get_groups
from meg_card.yuque_notice import forward_news
from meg_card.yuque_card import rjson
import threading
import random
import time


# 如果是群聊中仅@Bot, 无任何内容的逻辑
def empty_dialogue() -> str:
    choose_reply = ['干嘛, 没空陪你撩闲! 你待一边活泥巴去吧!', 
                    '这是表达个锤子? 艾特不说话, 等于耍流氓!', 
                    '心情好, 告诉你个秘密, 想要寻求帮助: /help',
                    '我在赚我的小目标, 十个亿以下的项目不要打扰我!',
                    f'礼貌点呦, 呼叫 \'{NICK_NAME}\', 看见会回复的!']
    res = random.choice(choose_reply)
    return res


# 群聊随机话术
def gchat_random_talk() -> str:
    choose_reply = ['好安静的群, 我出来活跃一下气氛~', 
                    '1, 2, 3, 4, 5... 我出来炸尸了!', 
                    '快乐的死法就是躺着数钱数到死也数不完。',
                    f'大噶好, 请叫我热爱僧活的{NICK_NAME}!',
                    '好无聊啊, 来个活人陪朕唠唠嗑!']
    res = random.choice(choose_reply)
    return res


# 跟Bot对话的能力
def bot_msg_talking(meta: dict, content: dict, flag: int = 1) -> dict:
    """
    flag: 1 means 'p2p' or @bot (default)
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

                # 情景5
                keyworks5 = ['/help', 'help', NICK_NAME]
                for i in keyworks5:
                    if i == info:
                        if meta['class'] == "@bot":
                            p = threading.Thread(target=__temp_task, args=(meta,))
                            p.start()
                        data = {'text': '诶~ 有人呼喊我?'}
                        break

            elif flag == 0:
                if info == "/help" or info == NICK_NAME:
                    if meta['class'] == "@bot":
                        p = threading.Thread(target=__temp_task, args=(meta,))
                        p.start()
                    data = {'text': gchat_random_talk()}
    return data


# Bot临时卡片与延迟删除 - 使用多线程
def __temp_task(meta):
    # print(f"param id: {meta}")
    content = rjson()
    msg_id = send_u_visible_msg(meta, content)
    if msg_id:
        time.sleep(60)
        del_u_visible_msg(msg_id)


# Bot推送卡片消息任务 - 使用多线程
def __send_task(args, kwargs):
    group_id = args['gid']
    group_name = args['gname']
    kwargs.update({
        "group_name": group_name
    })
    card = forward_news(**kwargs)
    send_card(group_id, card)

def card_sync(**kwargs):
    # Classification processing
    if kwargs['type'] == "main body":
        title_desc = f"'{kwargs['data']['belong_wiki']}' 发布了《{kwargs['data']['title']}》内容"
        update_time = f"北京时间 [{kwargs['data']['update_time']}]"
    elif kwargs['type'] == "comment":
        title_desc = f"用户 '{kwargs['data']['user']}' 在《{kwargs['data']['title']}》下进行了留言"
        update_time = f"最近更新 [{kwargs['data']['update_time']}]"

    # format saying
    data = {
         "hook_type": kwargs['data']['action_type'],
         "title_name": title_desc,
         "file_url": kwargs['data']['address_url'],
         "update_time": update_time
    }

    # action sync
    group_list = get_groups()
    send_list = []
    for i in group_list:
        p = threading.Thread(target=__send_task, args=(i, data))
        send_list.append(p)
        p.start()
    for i in send_list:
        i.join()
    # print("done")


if __name__ == '__main__':
    # card_sync(**data)
    # print(rjson())
    pass

