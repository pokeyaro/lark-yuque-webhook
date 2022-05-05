# -*- coding: UTF-8 -*-
"""
One-time use:
feishu app is connected with the back-end web service for the first time;
"""
# import os, sys; sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
from flask import Flask, Response, request, abort
from config.settings import PORT
from utils.decrypt_key import parse_event


app = Flask(__name__)

@app.route('/event/', methods=['POST'])
def callback_event():
    if (request.method != 'POST'):
        abort(405)
    else:
        encrypt = request.json.get('encrypt')
        data = parse_event(encrypt)
        challenge = data.get('challenge')
        if not challenge:
            abort(400)
        else:
            data = {'challenge': challenge}
            return Response(json.dumps(data), status=200, content_type='application/json')


@app.route('/bot/', methods=['POST'])
def callback_bot():
    if (request.method != 'POST'):
        abort(405)
    else:
        challenge = request.json.get('challenge')
        if not challenge:
            abort(400)
        else:
            data = {'challenge': challenge}
            return Response(json.dumps(data), status=200, content_type='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=PORT)

