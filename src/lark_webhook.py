# -*- coding: UTF-8 -*-
# import os, sys; sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import datetime
import requests
import json
# import time
from flask import Flask, Response, request, abort
from config.settings import PORT, APP_ID, APP_NAME
from src.public_func import bot_msg_talking, empty_dialogue
from open_api.bot_message import reply_meg
from utils.decrypt_key import parse_event
from utils.nt_hash import nt


def start(port: int):
    # chat_old, ctime_old = None, int(time.time())

    app = Flask(__name__)

    @app.route('/event/', methods=['POST'])
    def callback_event():
        # nonlocal chat_old, ctime_old
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
    
            # Verify event_type
            event_type = header_data.get('event_type')
            if event_type == "im.message.receive_v1":
                # Verify event_data
                event_data = data.get('event')

                # obsolete v1.0:
                # Deduplication of backend messages
                # chat_hash = nt(event_data.get('message').get('content'))
                # create_time = int(str(data.get('header').get('create_time')[:-3]))
                # if (chat_hash != chat_old) and (create_time > ctime_old):
               
                # get message content
                content = json.loads(event_data.get('message').get('content'))
                meg_id = event_data.get('message').get('message_id')

                # hook private chat bot message
                chat_type = event_data.get('message').get('chat_type')
                data = {}
                if chat_type == "p2p":
                    meg_type = event_data.get('message').get('message_type')
                    if meg_type != "text":
                        data = {'text': '人类迷惑行为大赏, 只接收Text!'}
                    else:
                        data = bot_msg_talking(content, 1)

                # messages in the hook group
                elif chat_type == "group":
                    mention_bot = event_data.get('message').get('mentions')
                    # @bot msg
                    if mention_bot:
                        for i in mention_bot:
                            if i['name'] == APP_NAME:
                                if content.get('text').strip() != i['key']:
                                    data = bot_msg_talking(content, 1)
                                else:
                                    data = {'text': empty_dialogue()}
                    # no @bot msg
                    else:
                        data = bot_msg_talking(content, 0)

                # send meg
                reply_meg(meg_id, msg_type="text", content=data)

                # obsolete v1.0:
                # print(f"chat_hash {chat_hash}, chat_old {chat_old}\ncreate_time {create_time}, ctime_old {ctime_old}")
                # chat_old, ctime_old = chat_hash, create_time
                return Response('"{}"', status=200, content_type='application/json')
            else:
                # HTTP 403 Forbidden.
                abort(403)
        else:
            # HTTP 405 Method Not Allowed.
            abort(405)

    app.run(host='0.0.0.0', debug=True, port=port)


if __name__ == '__main__':
    start(port=PORT)

