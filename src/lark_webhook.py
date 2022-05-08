# -*- coding: UTF-8 -*-
# import os, sys; sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import datetime
import requests
import json
import time
from flask import Flask, Response, request, abort
from config.settings import APP_ID, URLS, PORT, NICK_NAME, REPO_URL
from src.reply_content import bot_msg_talking, empty_dialogue, card_sync
from open_api.get_robot_info import get_app_info
from open_api.bot_message import reply_meg
from utils.decrypt_key import parse_event
from utils.nt_hash import nt


def start(port: int):
    # chat_old = None
    robot_info = None
    ctime_old = int(time.time())
    app = Flask(__name__)

    @app.route(URLS['events'], methods=['POST'])
    def callback_event():
        # nonlocal chat_old
        nonlocal robot_info, ctime_old
        if (request.method == 'POST'):
            # Received event ciphertext
            encrypt = request.json.get('encrypt')

            # Ciphertext parsing
            data = parse_event(encrypt)

            # Verify challenge (first conn)
            challenge = data.get('challenge')
            if challenge:
                data = {'challenge': challenge}
                return Response(json.dumps(data), status=200, content_type='application/json')

            # Get header info    
            header_data = data.get('header')

            # Verify app_id
            app_id = header_data.get('app_id')
            if app_id != APP_ID:
                # HTTP 400 Bad Request.
                abort(400)

            # Get app info
            if not robot_info:
                robot_info = get_app_info()

            # Verify event_type
            event_type = header_data.get('event_type')
            if event_type == "im.message.receive_v1":
                # Verify event_data
                event_data = data.get('event')

                # get sender open_id and chat_id
                sender = event_data.get('sender').get('sender_id').get('open_id')
                chat_id = event_data.get('message').get('chat_id')
                meta_info = {
                    'open_id': sender,
                    'chat_id': chat_id
                }

                # Deduplication of backend messages
                # chat_hash = nt(event_data.get('message').get('content'))
                create_time = int(str(data.get('header').get('create_time')[:-3]))
                # if (chat_hash != chat_old) and (create_time > ctime_old):
                if create_time > ctime_old:
                    # get message content
                    content = json.loads(event_data.get('message').get('content'))
                    meg_id = event_data.get('message').get('message_id')

                    # hook chat bot message type
                    chat_type = event_data.get('message').get('chat_type')
                    data = {}
                    # hook private chat bot message
                    if chat_type == "p2p":
                        meta_info.update({'class': 'p2p'})
                        data = bot_msg_talking(meta_info, content, 1)

                    # messages in the hook group
                    elif chat_type == "group":
                        meta_info.update({'class': '@bot'})
                        mention_bot = event_data.get('message').get('mentions')
                        # @bot msg
                        if mention_bot:
                            for i in mention_bot:
                                if i['name'] == robot_info['app_name']:
                                    if content.get('text').strip() != i['key']:
                                        real_msg = content.get('text').strip().replace(i['key'], "").strip()
                                        content = {'text': real_msg}
                                        data = bot_msg_talking(meta_info, content, 1)
                                    else:
                                        data = {'text': empty_dialogue()}
                        # no @bot msg
                        else:
                            data = bot_msg_talking(meta_info, content, 0)

                    # send meg
                    reply_meg(meg_id, msg_type="text", content=data)

                # limit update time
                ctime_old = create_time

                return Response('"{}"', status=200, content_type='application/json')
            else:
                # HTTP 403 Forbidden.
                abort(403)
        else:
            # HTTP 405 Method Not Allowed.
            abort(405)


    @app.route(URLS['larkbot'], methods=['POST'])
    def callback_bot():
        if (request.method != 'POST'):
            abort(405)
        else:
            data = request.json
            # Verify challenge (first conn)
            challenge = data.get('challenge')
            if challenge:
                res = {'challenge': challenge}
                return Response(json.dumps(res), status=200, content_type='application/json')

            # Handling comment likes for interactive cards
            action = data.get('action')
            if not action:
                abort(400)
            else:
                tag = action.get('tag')
                if tag != "button":
                    abort(400)
                else:
                    btn_id = action.get('value').get('button_id')
                    btn_type = action.get('value').get('button_type')
                    if btn_id == "bd_132529342258964":
                        real_type = {
                            'perfect': '哇, 💖 笔芯~',
                            'great': '诶呦, 不错呦~',
                            'common': '达咩达咩 🤬 '
                        }
                        text_content = real_type.get(btn_type)
                        res = {
                            'result': btn_type
                        }
                    else:
                        res = {}
                    # Reply message
                    reply_meg(
                        msg_id=data.get('open_message_id'),
                        msg_type="text",
                        content={'text': text_content}
                    )
                    ## TODO:
                    ### 可在此扩展数据持久化及统计分析功能
                    return Response(json.dumps(res), status=200, content_type='application/json')


    @app.route(URLS['yuque'], methods=['POST'])
    def callback_hook():
        global REPO_URL
        if (request.method != 'POST'):
            abort(405)
        else:
            # yuque-site test
            attr_md = request.json.get('markdown')
            if attr_md:
                if "测试消息" in attr_md.get('title'):
                    return Response(status=200, content_type='text/html')

            # check base url
            if not REPO_URL.endswith("/"):
                REPO_URL += "/"
            if not REPO_URL.startswith("http"):
                REPO_URL = "https://" + REPO_URL

            # content & type
            yq_data = request.json.get('data')
            webhook_type = yq_data.get('webhook_subject_type')

            # 当语雀用户发布或更新一篇文章
            if webhook_type in ("publish", "update"):
                # format yuque time
                yq_time_utc = yq_data.get('content_updated_at')
                yq_datetime = datetime.datetime.strptime(yq_time_utc, '%Y-%m-%dT%H:%M:%S.000Z')
                yq_time_local = (yq_datetime + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")

                # yuque basic info
                yq_title = yq_data.get('title')
                yq_wiki = yq_data.get('user').get('name')
                yq_url = REPO_URL + yq_data.get('path')

                # format yuque action
                if webhook_type == "publish":
                    yq_type = "内容发布（初版）"
                elif webhook_type == "update":
                    yq_type = "内容更新（迭代）"

                # data processing
                data_filter = {
                    'title': yq_title,
                    'belong_wiki': yq_wiki,
                    'address_url': yq_url,
                    'update_time': yq_time_local,
                    'action_type': yq_type
                }
                message = f"这是一条来自{NICK_NAME}的温馨提醒呦～\n北京时间 [{data_filter['update_time']}] 收录于 \'{data_filter['belong_wiki']}\' 中的《{data_filter['title']}》已完成{data_filter['action_type']}。"

                # collect
                data = { 
                    'code': 0,
                    'message': message,
                    'type': 'main body',
                    'data': data_filter
                }

            # 当语雀用户发表/更新/回复一条评论
            elif webhook_type in ("comment_create", "comment_update", "comment_reply_create"):
                # format yuque time
                yq_time_utc = yq_data.get('commentable').get('content_updated_at')
                yq_datetime = datetime.datetime.strptime(yq_time_utc, '%Y-%m-%dT%H:%M:%S.000Z')
                yq_time_local = (yq_datetime + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")

                # yuque basic info
                yq_user = yq_data.get('user').get('name')
                yq_title = yq_data.get('commentable').get('title')
                yq_url = REPO_URL + yq_data.get('path')

                # format yuque action
                if webhook_type == "comment_create":
                    yq_type = "新增评论 +1"
                elif webhook_type == "comment_update":
                    yq_type = "更新评论"
                elif webhook_type == "comment_reply_create":
                    yq_type = "回复评论"

                # data processing
                data_filter = {
                    'title': yq_title,
                    'user': yq_user,
                    'address_url': yq_url,
                    'update_time': yq_time_local,
                    'action_type': yq_type
                }
                message = f"这是一条来自{NICK_NAME}的温馨提醒呦～\n北京时间 [{data_filter['update_time']}]  用户 \'{data_filter['user']}\' 在《{data_filter['title']}》下方进行了留言（{data_filter['action_type']}）。"

                # collect
                data = { 
                    'code': 0,
                    'message': message,
                    'type': 'comment',
                    'data': data_filter
                }
            else:
                # print(request.json)
                abort(403)

            # message synchronization
            card_sync(**data)

            # request return value
            return Response(json.dumps({}), status=200, content_type='application/json')

    app.run(host='0.0.0.0', debug=True, port=port)


if __name__ == '__main__':
    start(port=PORT)

