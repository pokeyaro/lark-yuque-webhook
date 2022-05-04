# -*- coding: UTF-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
import json
import time
from flask import Flask, Response, request, abort
from settings import PORT, APP_ID
from open_api.bot_message import reply_meg
from utils.decrypt_key import parse_event
from utils.nt_hash import nt


def start(port: int):
    chat_old, ctime_old = None, int(time.time())

    app = Flask(__name__)

    @app.route('/event/', methods=['POST'])
    def callback_event():
        nonlocal chat_old, ctime_old
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
                # Deduplication of backend messages
                chat_hash = nt(event_data.get('message').get('content'))
                create_time = int(str(data.get('header').get('create_time')[:-3]))
                if (chat_hash != chat_old) and (create_time > ctime_old):
                    meg_type = event_data.get('message').get('message_type')
                    meg_id = event_data.get('message').get('message_id')                                                                                           
                    if meg_type != "text":
                        data = {'text': '人类迷惑行为大赏, 劳资只接收text!'}
                    else:
                        content = json.loads(event_data.get('message').get('content'))
                        if not content:
                            data = {'text': '风太大, 我听不清呀!'}
                        else:
                            info = content.get('text')
                            if info == "呵呵":
                                data = {'text': '呵呵你大爷!\n有本事再喝喝一句?'}
                            elif info in "你在干嘛呢?" or info in "在干嘛？":
                                data = {'text': '刷抖音!'}
                            else:
                                data = {'text': "你在讲啥子呦?"}
                    reply_meg(meg_id, msg_type="text", content=data)
                # print(f"chat_hash {chat_hash}, chat_old {chat_old}\ncreate_time {create_time}, ctime_old {ctime_old}")
                chat_old, ctime_old = chat_hash, create_time
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

