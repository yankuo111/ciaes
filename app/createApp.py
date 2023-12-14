#!/usr/bin/python3

# @File: createApp.py

# -*-coding:utf-8-*-

# @Author:Guan_pc

# @Time: 2023年03月30日15时

# 说明:

import logging.handlers
import os

import sqlalchemy
from flask import Flask, make_response, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from app.config import sqlalchemyCommitOnTearoowm, database, sqlalchemyEcho, secretKey, logDir
from database.config import mysqlurl

# with sqlalchemy.create_engine(
#         mysqlurl,
#         isolation_level='AUTOCOMMIT'  #
# ).connect() as connection:
#     databases = connection.execute('show databases').fetchall()
#     if (database,) not in databases:
#         connection.execute(f'CREATE DATABASE {database} charset="utf8"')
app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config["SQLALCHEMY_DATABASE_URI"] = f'{mysqlurl}/{database}'
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = sqlalchemyCommitOnTearoowm
app.config['SQLALCHEMY_ECHO'] = sqlalchemyEcho
app.config['SQLALCHEMY_POOL_SIZE'] = 100
app.config['SECRET_KEY'] = secretKey
# mysqlLink = SQLAlchemy(app)

if os.path.exists(os.path.split(logDir)[0]) == False:
    os.makedirs(os.path.split(logDir)[0])
handler = logging.handlers.TimedRotatingFileHandler(filename=logDir, when='midnight',
                                                    backupCount=30,
                                                    encoding='utf8')
handler.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s'))
app.logger.addHandler(handler)
logging.getLogger().setLevel(logging.INFO)


# socketio = SocketIO()
# socketio.init_app(app, cors_allowed_origins='*')


@app.after_request
def after_request(resp):  # 对app下收到的所有请求之后对请求做进一步处理。
    # from app.workMethod.historyWork import save_history
    resp = make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'content-type,token'
    try:
        if resp._status_code == 200:
            app.logger.info(request.endpoint)
            return resp
    except:
        return resp


if __name__ == '__main__':
    a = 1
