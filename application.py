#!/usr/bin/python3

# @File: application.py

# -*-coding:utf-8-*-

# @Author:Guan_pc

# @Time: 2023年03月30日17时

# 说明:
import os
# os.environ["CUDA_VISIBLE_DEVICES"]='0'
import asyncio
import threading
from flask import Flask, render_template
from app.appWork.chatWork import main
from app.authVerify import verify
from app.chatSession import chatSession
from app.createApp import app
app.register_blueprint(verify, url_prefix='/verify')
app.register_blueprint(chatSession, url_prefix='/chatSession')

web = Flask(__name__,
            static_folder='./dist',  # 设置静态文件夹目录
            template_folder="./dist",
            static_url_path=""
            )


@web.route('/')
def index():
    return render_template('index.html', name='index')



if __name__ == '__main__':
    flask_thread = threading.Thread(target=app.run, kwargs = {
        'host' : '0.0.0.0',
        'port': 6060,
        'debug': True,
        'use_reloader':False,
        'threaded': False
    })
    flask_thread.start()


    web_thread = threading.Thread(target=web.run, kwargs={
        'host': '0.0.0.0',
        'port': 21359,
        'debug': True,
        'use_reloader': False,
        'threaded': True
    })
    web_thread.start()

    asyncio.run(main())
    # app.run(host='0.0.0.0', port=4000, debug=True, use_reloader=False, threaded=True)
    # socketio.run(app, host='0.0.0.0', port=4000, debug=True,use_reloader=False)
